# Hidden properies of super class can not be accessed directly with in the subclass.
class X:
    __a=1000
    def __init__(self):
        self.__b=2000
    def __m1(self):
        print("in m1 of x")
class Y(X):
    __c=3000
    def __init__(self):
        self.__d=4000
        super().__init__()
    def __m2(self):
        print("in m2 of y")
    def display(self):
        print(Y.__c)
        print(self.__d)
        self.__m2()
        print(Y.__a)
        print(self.__b)
        self.__m1()
y1=Y()
y1.display()
