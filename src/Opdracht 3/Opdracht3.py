import os


class Opdracht3():
    path = ""

    def __init__(self, path):
        self.path = path
        self.getcontents(self.path)

    def getcontents(self, path):
        for dirname, dirnames, filenames in os.walk(path):
            # print path to all subdirectories first.
            for subdirname in dirnames:
                print(os.path.join(dirname, subdirname))

            # print path to all filenames.
            for filename in filenames:
                print(os.path.join(dirname, filename))


Opdracht3("../")
