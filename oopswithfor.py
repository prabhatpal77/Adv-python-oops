# use of instanceOf and *args. and use of logic in method.
class X:
    def add(self, instanceOf, *args):
        if instanceOf=='int':
            result=0
        if instanceOf=='str':
            result=''
        for i in args:
            result=result+i
        print(result)
x1=X()
x1.add('int', 10, 20, 30)
x1.add('str', 'prabhat', 'pal')
