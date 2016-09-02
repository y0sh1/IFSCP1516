import argparse
import os


class opdracht8():
    parser = argparse.ArgumentParser(description='Dit is Opdracht 3, IFSCP 1516')
    parser.add_argument('-opdracht1', action="store_true", help="Start opdracht 1")
    parser.add_argument('-opdracht2', action="store_true", help="Start opdracht 2")
    parser.add_argument('-opdracht3', action="store_true", help="Start opdracht 3, also needs -p")
    parser.add_argument('-opdracht4', action="store_true", help="Start opdracht 4, also needs -p and -d")
    parser.add_argument('-opdracht5', action="store_true", help="Start opdracht 5, also needs -p")
    parser.add_argument('-opdracht6', action="store_true", help="Start opdracht 6")
    parser.add_argument('-opdracht7', action="store_true", help="Start opdracht 7, also needs -u")
    parser.add_argument('-p', action="store", help="Start opdracht 3")
    parser.add_argument('-d', action="store", help="Start opdracht 3")
    parser.add_argument('-u', action="store", help="Start opdracht 3")
    args = parser.parse_args()

    def __init__(self):
        self.args = self.parser.parse_args()
        if self.args.opdracht1:
            os.system("python './src/Opdracht 1/Opdracht1.py'")
        elif self.args.opdracht2:
            os.system("python './src/Opdracht 2/Opdracht2.py'")
        elif self.args.opdracht3 and self.args.p:
            os.system("python './src/Opdracht 3/Opdracht3.py' -p " + self.args.p)
        elif self.args.opdracht4 and self.args.p and self.args.d:
            os.system("python './src/Opdracht 4/Opdracht4.py' -p " + self.args.p + " -d " + self.args.d)
        elif self.args.opdracht5 and self.args.p:
            os.system("python './src/Opdracht 5/Opdracht5.py' -p " + self.args.p)
        elif self.args.opdracht6:
            os.system("python './src/Opdracht 6/Opdracht6.py'")
        elif self.args.opdracht7 and self.args.u:
            os.system("python './src/Opdracht 7/Opdracht7.py' -u " + self.args.u)
        else:
            print("No valid combination of parameters set. Please use --help for more info")

if __name__ == "__main__":
    opdracht8()