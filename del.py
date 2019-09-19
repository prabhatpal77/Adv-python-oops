# Del is keyword, which removes the given reference variable from memory location.
# When ever the reference variable is deleted from memory location then internally that variable pointed
# object reference count is decremented by 1.
class X:
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
del x1
del x2
del x3
