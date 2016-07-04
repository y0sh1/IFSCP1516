import argparse
import mimetypes
import os
import exifread
import geojson
import time

parser = argparse.ArgumentParser(description='Dit is Opdqdracht 5, IFSCP 1516')
parser.parse_args()

args = parser.parse_args()

class opdracht5():
    path = "./src/Opdracht 5/images"

    # Init Class
    def __init__(self):
        files = self.getJpegsFromDir(self.path)
        # self.printJpegInfo(files)
        gpsdict = self.generateGPSJSON(files)
        self.WriteFile(self.GPSDictToGeoJSON(gpsdict))
        print ("export completed, please check report.html")

    def getJpegsFromDir(self, dir):
        jpegs = []
        files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
        for file in files:
            if str(mimetypes.guess_type(file)).__contains__("image/jpeg"):
                jpegs.append(file)
        return files

    # Extract GPS info from files
    def generateGPSJSON(self, files):
        GPSfiles = {}
        for file in files:
            fullpath = os.path.join(self.path, file)
            f = open(fullpath, 'rb')
            tags = exifread.process_file(f)
            f.close()
            print(str(file) + " is " + str(tags['EXIF ExifImageWidth']) + " x " + str(tags['EXIF ExifImageLength']))
            print("Laatst aangepast op: " + str(time.ctime(os.path.getmtime(fullpath))))
            print("Aangemaakt op: " + str(time.ctime(os.path.getctime(fullpath))))
            GPS = (self.get_exif_location(tags))
            GPSfiles[file] = {"lat": GPS[0], "long": GPS[1]}
        return GPSfiles

    # Convert Custom GPS data to GeoJson
    def GPSDictToGeoJSON(self, input):
        points = []
        features = []
        for item in input:
            features.append(geojson.Feature(geometry=geojson.Point((input[item]['long'], input[item]['lat']))))
        return geojson.FeatureCollection(features)

    # Write stuff to a file
    def WriteFile(self, contents):
        file = open("places.json", 'w+')
        file.write(str(contents))
        file.close()


    # From https://gist.github.com/snakeye/fdc372dbf11370fe29eb
    # Used to extract exif info
    def get_exif_location(self, exif_data):
        """
        Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)
        """
        lat = None
        lon = None

        gps_latitude = self._get_if_exist(exif_data, 'GPS GPSLatitude')
        gps_latitude_ref = self._get_if_exist(exif_data, 'GPS GPSLatitudeRef')
        gps_longitude = self._get_if_exist(exif_data, 'GPS GPSLongitude')
        gps_longitude_ref = self._get_if_exist(exif_data, 'GPS GPSLongitudeRef')

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = self._convert_to_degress(gps_latitude)
            if gps_latitude_ref.values[0] != 'N':
                lat = 0 - lat

            lon = self._convert_to_degress(gps_longitude)
            if gps_longitude_ref.values[0] != 'E':
                lon = 0 - lon

        return lat, lon

    # From https://gist.github.com/snakeye/fdc372dbf11370fe29eb
    def _get_if_exist(self, data, key):
        if key in data:
            return data[key]

        return None

    # From https://gist.github.com/snakeye/fdc372dbf11370fe29eb
    def _convert_to_degress(self, value):
        """
        Helper function to convert the GPS coordinates stored in the EXIF to degress in float format
        :param value:
        :type value: exifread.utils.Ratio
        :rtype: float
        """
        d = float(value.values[0].num) / float(value.values[0].den)
        m = float(value.values[1].num) / float(value.values[1].den)
        s = float(value.values[2].num) / float(value.values[2].den)

        return d + (m / 60.0) + (s / 3600.0)

opdracht5()