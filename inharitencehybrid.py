# Hybrid inharitence:- Combination of single, multilevel, hyrarchal, multiple inharitence is known as hybrid inharitence.
class X:
    def m1(self):
        print("m1 in x")
class Y:
    def m2(self):
        print("m2 in Y")
class Z:
    def m3(self):
        print("m3 in z")
class A(X, Y):
    def m4(self):
        print("m4 in a")
class B(Y, Z):
    def m5(self):
        print("m5 in b")
class M(A, B):
    def m6(self):
        print("m6 in m")
m7=M()
m7.m1()
m7.m2()
m7.m3()
m7.m4()
m7.m5()
m7.m6()
