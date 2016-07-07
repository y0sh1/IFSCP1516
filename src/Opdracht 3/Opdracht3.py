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
                if '.git' in dirnames:
                    dirnames.remove('.git')
                print(os.path.join(dirname, subdirname))

            # print path to all filenames.
            for filename in filenames:
                print(os.path.join(dirname, filename))

if __name__ == "__main__":
    Opdracht3("../")
