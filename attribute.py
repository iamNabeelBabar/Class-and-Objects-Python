class Car:
    color = 'red' # -----> class attribute
    price = 2000000
    location = 'Pakistan'


car1 = Car()  # car1 is the object of Car() class

print(car1.color, car1.price, car1.location)


car2 = Car()
car2.name = 'mercedes' #----> object attribute
car2.color = 'green'   #----> object attribute

print(car2.name, car2.color, car2.price, car2.location)
