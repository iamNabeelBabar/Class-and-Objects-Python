# Object Oriented Programming

# Class & Object:
# We create a class with class attributes (also known as class variables).

# In this example, I will create a class where all employees have
# the same country and salary:

class Employee:          # Employee is a class
    country = "Pakistan" # Class Attribute (Class Variable)
    salary = 1200000     # Class Attribute (Class Variable)

# Now I will create objects of this class.
# All employees belong to Pakistan and have the same salary:

employee1 = Employee()              # employee1 is an object of the Employee class
employee1.name = 'Nabeel'           # Instance Attribute assigned to employee1
print(employee1.country, employee1.salary)  # This will print employee1's country and salary

employee2 = Employee()              # employee2 is another object of the Employee class
employee2.name = 'Ali'              # Instance Attribute assigned to employee2
print(employee2.country, employee2.salary)  # This will print employee2's country and salary


# -----------> In the above code and comments, we learned that 
#              all objects created from the Employee class will 
#              have the same 'country' and 'salary' because these 
#              are class attributes (shared by all objects).
