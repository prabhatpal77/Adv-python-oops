# del list object.
class X:
    def __init__(self):
        print("in constructor of x")
    def display(self):
        print("welome")
    def __del__(self):
        print("in destructor of x")
p=[X(), X(), X()]
del p[2]
del p
