
class Calculator:
    
    def __init__(self, num1, num2):
        
        self.num1 = num1
        self.num2 = num2
        
    def sum(self):
        self.result = self.num1 + self.num2
        return f'The sum of {self.num1} and {self.num2} is {self.result}'
    
    
    def subtract(self):
        self.result = self.num1 - self.num2
        return f'The subtraction of {self.num1} and {self.num2} is {self.result}'
    
    def multiply(self):
        self.result = self.num1 * self.num2
        return f'The multiplication of {self.num1} and {self.num2} is {self.result}'
    
    def divide(self):
        self.result = self.num1 / self.num2
        return f'The division of {self.num1} and {self.num2} is {self.result}'
    

print("Please Enter two numbers")
number1 = int(input('Enter number1: '))
number2 = int(input('Enter number 2: '))

calculator = Calculator(number1, number2)
print("What do you wan to calculate: ")
print('sum(1), subtraction(2), multiplication(3), division(4)')
action = int(input())
if action == 1:
    print(calculator.sum())
elif action == 2:
    print(calculator.subtract())
elif action == 3:
    print(calculator.multiply())
elif action == 4:
    print(calculator.divide())
else:
    print('wrong input')


print('program end')