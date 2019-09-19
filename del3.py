# del keyword by emp app.
class Emp:
    """emp app"""
    empcnt=0
    def __init__(self, eid, ename, eadd, esal):
        self.eid=eid
        self.ename=ename
        self.eadd=eadd
        self.esal=esal
        Emp.empcnt=Emp.empcnt+1
    def __del__(self):
        Emp.empcnt=Emp.empcnt-1
e1=Emp(1122,"pal","ayodhya",3000.00)
e2=Emp(1010,"prabhat","bikapur",5000.00)
e3=Emp(1212,"aryan","noida",6000.00)
del e2
print("total no of emplayees are", Emp.empcnt)
