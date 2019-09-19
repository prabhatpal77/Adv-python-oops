# Object class is a predefined class which is define built-in methodes.
# Object class is a super class for every class in python.
# Object class properties we can access in every class directly.
# Object class properties we can access through every class reference variable.
class X:
    def m1(self):
        print("in m1 of x")
class Y(X):
    def m2(self):
        print("in m2 of y")
print(X.__bases__)
print(Y.__bases__)
y1=Y()
y1.m1()
y1.m2()
p=y1.__hash__()
print(p)
