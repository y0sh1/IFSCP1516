import argparse
import os


class Opdracht3():
    parser = argparse.ArgumentParser(description='Dit is Opdracht 3, IFSCP 1516')
    parser.add_argument('-p', action="store", help="Path to the to scan directory", required=True)
    parser.parse_args()
    path = ""

    def __init__(self):
        args = self.parser.parse_args()
        if args.p:
            self.path = args.p
        self.getcontents(self.path)

    def getcontents(self, path):
        for dirname, dirnames, filenames in os.walk(path):
            # print path to all subdirectories first.
            for subdirname in dirnames:
                if '.git' in dirnames:
                    dirnames.remove('.git')
                print(os.path.join(dirname, subdirname))

            # print path to all filenames.
            for filename in filenames:
                print(os.path.join(dirname, filename))

if __name__ == "__main__":
    Opdracht3()
