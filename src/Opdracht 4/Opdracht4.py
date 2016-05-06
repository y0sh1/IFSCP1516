import os
import argparse

parser = argparse.ArgumentParser(description='Dit is Opdracht 4, IFSCP 1516')
parser.add_argument('-p', action="store", dest="PathToScan", help="Path to the to scan directory")
parser.parse_args()

args = parser.parse_args()


class Opdracht4:
    path = ""
    foundpaths = []

    def __init__(self, path):
        self.path = path
        print(self.getcontents())

    def getcontents(self):
        contents = os.listdir(self.path)
        return contents

Opdracht4(args.PathToScan)

