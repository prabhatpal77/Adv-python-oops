# Multiple inhharitence another e.g.
class X:
    def m1(self):
        print("in m1 of x")
    def display(self):
        print("welcome from x")
class Y:
    def m2(self):
        print("in m2 of y")
    def display(self):
        print("welcome from y")
class Z(X,Y):
    def m3(self):
        print("in m3 of z")
z1=Z()
q=z1.__hash__()
print(q)
z1.m1()
z1.m2()
z1.m3()
z1.display()
