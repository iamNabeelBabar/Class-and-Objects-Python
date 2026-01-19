class Employee:
    
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
        
    def print_details(self):
        return f"The salary of {self.name} is {self.salary} and department is {self.department}"

employee1 = Employee("Nabeel", 20000, "AI")
employee2 = Employee("bilawal", 30000, "AI")

print(employee1.print_details())
print(employee2.print_details())
