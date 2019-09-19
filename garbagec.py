# The concept of removing unused reference objects from the memory location is known as a garbage collection.
# For every object python interpretor internally maintain reference count.
# Total no. of reference variables which are pointed an object is known as a reference count of the object.
# The reference count of nay object become zero then we call that object as a unused unreffered object.
# At a time of execution of the program if any object reference count become zero then internally python calls G.C.
# Garbage collections is a predefine program or background thread, which removes the unused ar unreferenced onject from
# the memory location.
class X:
    def m1(self):
        print("in m1 of X")
    def m2(self):
        print("in m2 of X")
x1=X()
print(x1)
x1.m1()
x1.m2()
x2=X()
print(x2)
x2.m1()
x2.m2()
