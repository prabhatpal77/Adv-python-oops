# del keyword.
class X:
    def __init__(self):
        print("in constructor of x")
    def display(Self):
        print("welcome")
    def __del__(self):
        print("in destructor of x")
x1=X()
x1.display()
del x1
X().display()
