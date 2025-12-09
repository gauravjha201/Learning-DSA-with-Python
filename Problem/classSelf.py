class employee:
    language="python"
    salary=1200000

    def getinfo(self):
        print(f"language is {self.language} and salary is {self.salary}")
    def greet(self):
        print("Good Morning")
Gaurav=employee()
Gaurav.language="javaScript" #this is an instance attribute
Gaurav.getinfo()
Gaurav.greet()
# employee.getinfo(Gaurav)