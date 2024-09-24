class Employees:
    def __init__(self,name,email,dept,salary):
        self.name=name
        self.email=email
        self.dept=dept
        self.salary=salary


emp1=Employees('Neha','neha@gmail.com','software Enginner','50000')
emp2=Employees('Nidhi','nidhi@gmail.com','doctor','60000')
emp3=Employees('Nandini','nandini@gmail.com','software Enginner','70000')

print(emp1.name)
print(emp2.email)
print(emp3.dept)