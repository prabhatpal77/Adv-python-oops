# __init__() is constructor and __del__() is constructor.
class X():
    def __init__(self):
        print("in constructor of x")
    def __del__(self):
        print("in destructor of x")
x1=X()
print(x1)
x2=x1
print(x2)
x3=x2
print(x3)
x1=X()
print(x1)
x2=X()
print(x2)
x3=X()
print(x3)
