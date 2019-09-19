# Abstraction:- The concept of hidding the properties of a class from outside of the class is known as a abstraction.
# Any property of a class which is preceeded by __ is going to be hidden from the class.
# Hidden properties of a class can not be accessing directly of the class.
class X:
    __a=1000
    def __init__(self):
        self.__b=2000
    def __m1(self):
        print("in m1 of x")
    def display(self):
        print(X.__a)
        print(self.__b)
        self.__m1()
x1=X()
x1.display()
print(X.__a)
print(x1.__b)
x1.__m1()
