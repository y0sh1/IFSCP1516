import os
import argparse
import magic
from shutil import copy2
import traceback

parser = argparse.ArgumentParser(description='Dit is Opdracht 4, IFSCP 1516')
parser.add_argument('-v', action="store_true", dest="verbose", help="Turn on verbosity")
parser.add_argument('-p', action="store", help="Path to the to scan directory", required=True)
parser.add_argument('-d', action="store", help="Set path to copy to", required=True)
parser.parse_args()

args = parser.parse_args()


class Opdracht4:
    path = ''
    dest = ''

    def __init__(self):
        args = parser.parse_args()
        self.path = args.p
        self.dest = args.d
        fullpaths = self.getContents(self.path)
        sortedmimes = self.selectCorrectMIMEs(fullpaths)
        self.copyFilesToTypeDirs(sortedmimes[0], sortedmimes[1], sortedmimes[2], sortedmimes[3])

    def getContents(self, path):
        fullpaths = []
        for dirname, dirnames, filenames in os.walk(path):
            if '.git' in dirnames:
                dirnames.remove('.git')
            if '.idea' in dirnames:
                dirnames.remove('.idea')
            for file in filenames:
                fullpaths.append(os.path.join(dirname, file))
        return fullpaths

    # MIME types from http://filext.com/faq/office_mime_types.php
    def selectCorrectMIMEs(self, paths):
        sortedFilesPDF = []
        sortedFilesZIP = []
        sortedFilesWord = []
        sortedFilesExcel = []
        for file in paths:
            mime = magic.from_file(file, mime=True)
            if mime == "application/pdf":
                sortedFilesPDF.append(file)
            elif mime == "application/zip":
                sortedFilesZIP.append(file)
            elif mime == "application/msword":
                sortedFilesWord.append(file)
            elif mime == "application/vnd.ms-excel":
                sortedFilesExcel.append(file)
        return sortedFilesWord, sortedFilesExcel, sortedFilesZIP, sortedFilesPDF

    def copyFilesToTypeDirs(self, sortedFilesWord, sortedFilesExcel, sortedFilesZIP, sortedFilesPDF):
        try:
            if len(sortedFilesPDF) != 0:
                destdirPDF = os.path.join(self.dest, "PDF")
                if not os.path.isdir(destdirPDF):
                    os.makedirs(destdirPDF)
                for pdf in sortedFilesPDF:
                    copy2(pdf, destdirPDF)
                    print("Copied " + pdf)
            if len(sortedFilesZIP) != 0:
                destdirZIP = os.path.join(self.dest, "ZIP")
                if not os.path.isdir(destdirZIP):
                    os.makedirs(destdirZIP)
                for zip in sortedFilesZIP:
                    copy2(zip, destdirZIP)
                    print("Copied " + zip)
            if len(sortedFilesWord) != 0:
                destdirWORD = os.path.join(self.dest, "WORD")
                if not os.path.isdir(destdirWORD):
                    os.makedirs(destdirWORD)
                for word in sortedFilesWord:
                    copy2(word, destdirWORD)
                    print("Copied " + word)
            if len(sortedFilesExcel) != 0:
                destdirEXCEL = os.path.join(self.dest, "EXCEL")
                if not os.path.isdir(destdirEXCEL):
                    os.makedirs(destdirEXCEL)
                for excel in sortedFilesExcel:
                    copy2(excel, destdirEXCEL)
                    print("Copied " + excel)

        except Exception:
            print("Oops! :(\n" + traceback.format_exc())
        return 0

if __name__ == "__main__":
    Opdracht4()