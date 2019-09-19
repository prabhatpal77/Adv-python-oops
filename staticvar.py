# The static variable which are declared directly with in the class outside of all methods are known as static variables.
# The data which is common for every all objects is recommended to represent by using static variable.
# From the static variable of a class memory will be allocated automatically only once.
# Static variable of one class we can access with in the same class by using class name.
# Static variable of one class we can access from outside of the class by using classname or reference variable.
# Static variables we can also call as a claa variables.
class Test:
    """sample class to test atatic variables"""
    a=1000
    b=2000
    def display(self):
        print(Test.a)
        print(Test.b)
t1=Test()
t1.display()
print(Test.a)
print(Test.b)
print(t1.a)
print(t1.b)
