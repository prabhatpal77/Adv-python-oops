# Hierarchal inharitence:- The concept of inhariting the properties from 1 class into multiple classes sepratly
# is known as a hierarchal inharitance.
class X:
    def m1(self):
        print("in m1 of x")
class Y(X):
    def m2(self):
        print("in m2 of y")
class Z(X):
    def m3(self):
        print("in m3 of z")
y1=Y()
p=y1.__hash__()
print(p)
y1.m1()
y1.m2()
z1=Z()
q=z1.__hash__()
print(q)
z1.m1()
z1.m3()
