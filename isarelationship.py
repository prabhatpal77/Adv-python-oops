# is a relationship:- The concept of using the properties of 1 class into another class directly like
# some class member is known as a inharitance or is a relationship.
# The class which is extended by another class is known as super class or base class.
# The class which is extending another class is known as a sub class or derived class.
# We can access the super class properties directly within the subclass like as a subclass members.
class X:
    a=1000
    def m1(self):
        print("in m1 od X")
class Y(X):
    b=2000
    def __init__(self):
        self.c=3000
    def m2(self):
        print("in m2 of Y")
    def display(self):
        print(Y.b)
        print(self.c)
        self.m2()
        print(Y.a)
        self.m1()
y1=Y()
y1.display()
