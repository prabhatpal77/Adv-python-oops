# The variables which are declared directly within method body are known as local variables.
# The data which is required to use within a perticuler operation is recommended to represent by using local variables.
# Call the local variables of a method memory will be allocated when ever we make it method call.
# With respect to every time method call sepratte copy of memory will be allocated for local varibles.
# Local variables of one method we can not access from outside of that method.
class Test:
    def m1(self):
        a=1000
        b=2000
        print(a)
        print(b)
    def m2(self):
        c=3000
        d=4000
        print(c)
        print(d)
        print(a)
        print(b)
t1=Test()
t1.m1()
t2=Test()
t2.m2()
# name error: 'name' a is not defineshould come.
