# Non-static variable:- The variable which are declared within the class anywhere by using self. are known as
# non-static variable.
# The data which is seprate for every object is recommended to represent by using non-static variables.
# For all the non-static variable of a class memory will be allocated within the objects.
# Non-static variables of one class we can access with in the same class by using self.
# With respect to every object seprate copy of the memory will be allocated for non-static variables.
# Non-static variables of one class we can access from aut side of the class by using reference variables.
# Non-static variables we can also call as a instance variable.
class Test:
    """test non-static variables"""
    def insert(self):
        self.a=1000
        self.b=2000
    def display(self):
        print(self.a)
        print(self.b)
t1=Test()
print(t1)
t1.insert()
t1.display()
print(t1.a)
print(t1.b)
t2=Test()
print(t2)
t2.insert()
t2.display()
print(t2.a)
print(t2.b)
