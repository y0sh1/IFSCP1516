import os
import argparse
import magic
import logging
import shutil

parser = argparse.ArgumentParser(description='Dit is Opdracht 4, IFSCP 1516')
parser.add_argument('-v', action="store_true", dest="verbose", help="Turn on verbosity")
parser.add_argument('-p', action="store", dest="PathToScan", help="Path to the to scan directory", required=True)
parser.add_argument('-d', action="store", dest="DestinationPath", help="Set path to copy to", required=True)
parser.parse_args()

args = parser.parse_args()


class Opdracht4:
    path = ''

    def __init__(self):
        self.path = str(args['PathToScan'])
        files = self.getContents()
        logger = logging.getLogger('IFSCP')
        if args.verbose:
            logger.setLevel(logging.DEBUG)
            logging.debug("Debug Set")
        self.copyFiles(self.getTypesFromPaths(self.getContents()))

    def getContents(self):
        contents = os.listdir(self.path)
        for item in contents:
            if not os.path.isfile(os.path.join(os.getcwd(), item)):
                contents.remove(item)
        return contents

    def getTypesFromPaths(self, paths):
        fileTypesPerPath = {}
        for path in paths:
            fileTypesPerPath[path] = magic.from_file(path, mime=True)
        return fileTypesPerPath

    def copyFiles(self, fileTypes, destination):
        for key, value in fileTypes:
            fileToWriteTo = os.path.join(destination, value)
            sourceFileName = os.path.split(key)
            if not os.path.exists(fileToWriteTo):
                os.makedirs(fileToWriteTo)
            shutil.copy2(key, os.path.join(fileToWriteTo, sourceFileName))

Opdracht4()