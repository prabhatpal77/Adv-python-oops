# We can access the hidden properties of a super class within the subclass through special syntax.
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
        print(self._X__a)
        print(self._X__b)
        self._X__m1()
y1=Y()
y1.display()
