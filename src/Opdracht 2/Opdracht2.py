class HelloWorld:
    greeting = ""

    def __init__(self):
        self.greeting = "hello world"

    def function1(self):
        if self.greeting == "hello world":
            print(self.greeting)
        return True

    def function2(self):
        if 1 == 1:
            print(self.greeting)
            return False
        else:
            return True

HelloWorld().function1()
HelloWorld().function2()
