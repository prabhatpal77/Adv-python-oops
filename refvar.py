# Through the reference variable we can put the data into the object, we can get the data from the object
# and we can call the methods on the object.
# We can creste a number of objects for a class. Two different object of a same class or different classes
# does not contain same address.
class Test:
    """sample class to test object"""
    def display(self):
        print("welcome")
print(Test.__doc__)
t1=Test()
print(t1)
t1.display()
t2=Test()
print(t2)
t2.display()
