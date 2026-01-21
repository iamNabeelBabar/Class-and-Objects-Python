
class Student:
    
    section = 'A5' #class property
    
    def __init__(self, name, age):
        
        self.name = name  #instance property
        self.age = age
    
    def full_detail(self):
        return f'your name is {self.name} and age is {self.age}'
        
student1 = Student('Ali', 20)

print(student1.name)
print(student1.age)
print('Section is: ',student1.section)

print(student1.full_detail())