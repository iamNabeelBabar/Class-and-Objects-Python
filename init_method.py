class Student:
    
    def __init__(self, name, programme, roll_number):
        self.name = name
        self.programme = programme
        self.roll_number = roll_number
        print(f"student {self.name} has been created.")
        

student1 = Student("Nabeel", "Artificial Intelligence", 201)
