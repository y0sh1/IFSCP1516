import sys


class opdracht1():
    def __init__(self):
        if __name__ == "__main__":
            self.main()

    def main(self):
        if self.ispython3():
            print("Hello Python 3!")
        else:
            print("Hello Python 2!")

    def ispython3(self):
        if sys.version_info > (3, 0):
            return True
        else:
            return False


opdracht1()
