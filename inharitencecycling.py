# Cycling inharitence:- The concept of inhariting the properties subclass to super class is known as cycling inharitence.
# Python does not support cycling inharitence.
class X(Z):
    def m1(self):
        print("in m1 od x")
class Y(X):
    def m2(self):
        print("in m2 of y")
class Z(Y):
    def m3(self):
        print("in m3 of z")
z1=Z()
# erroe: z is not defined.
