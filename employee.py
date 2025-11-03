class Employee:
    def __init__(self, empid, name, department, salary):
        self.empid = empid
        self.name = name
        self.department = department
        self.salary = salary
    def displayEmployee(self):
        print("Employee ID:", self.empid)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)
emp1 = Employee(12345, "Ramakrishnan", "Electrical", 34000)
emp1.displayEmployee()
