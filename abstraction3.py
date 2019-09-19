# We can access the hidden properties of a class from outside of the class through spacial syntax.
class X:
    __a=1000
    def __init__(self):
        self.__b=2000
    def __m1(self):
        print("in m1 of x")
x1=X()
print(x1._X__a)
print(x1._X__b)
x1._X__m1()
