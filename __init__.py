# class Test:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

# t1=Test(5,6)
# t2=Test(2,3)
# print(t1.a,t1.b)
# print(t2.a,t2.b)


class employee:
    def __init__(self,empid=None,name=None,salary=None):
        self.empid=empid
        self.name=name
        self.salary=salary
    def setempid(self,empid):
        self.empid=empid
    def setname(self,name):
        self.name=name
    def setsalary(self,salary):
        self.salary=salary
    def getempid(self):
        return self.empid
    def getname(self):
        return self.name
    def getsalary(self):
        return self.salary
e1=employee()
e2=employee(1,"Gaurav",2499999)
e1.setempid(2)
e1.setname("Sachin")
e1.setsalary(2499999)
print(e1.getempid(),e1.getname(),e1.getsalary())
print(e2.getempid(),e2.getname(),e2.getsalary())


