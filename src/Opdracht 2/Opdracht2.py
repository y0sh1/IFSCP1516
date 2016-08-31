import sys

class HelloWorld:
    greeting = ""

    def __init__(self):
        self.greeting = "hello world"

    def ifStatement1(self):
        if self.greeting == "hello world":
            print(self.greeting)
        return True

    def ifStatement2(self):
        if 1 == 1:
            print(sys.version_info)
            return False
        else:
            return True

    def forLooping1(self):
        try:
            wordslist = ['koekje', 'fiets', 'aardappel']
            for item in wordslist:
                print(item)
                return True
        except Exception as e:
            print("Foutje! :(\n" + e)

    def inAndOutput(self):
        try:
            filewrite = open("inandoutput.txt", "w")
            filewrite.write("Write some text")
            filewrite.close()
            fileread = open("inandoutput.txt", "r")
            print(fileread.readlines())
            fileread.close()
        except Exception as e:
            print("Foutje! :(\n" + e)

if __name__ == "__main__":
    HelloWorld().ifStatement1()
    HelloWorld().ifStatement2()
    HelloWorld().forLooping1()
    HelloWorld().inAndOutput()
    print("seems oke :)")
