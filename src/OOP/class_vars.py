# class Dog:
#     counter = 0
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Dog.counter += 1


# first_pet = Dog('Tedy', 2)
# second_pet = Dog('Bergi', 4)
# third_pet = Dog('Lori', 5)

# print(first_pet.__dict__)
# print(first_pet.counter)
# print(second_pet.counter)
# print(third_pet.counter)

# print(Dog.counter)


# class Dog:
#     __counter = 0
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Dog.__counter += 1



# print(Dog._Dog__counter)
# print(Dog.__dict__)

# my_pet = Dog('Tedy', 2)
# print(type(my_pet).__name__)

# print(Dog.__module__) # where the class is defined

class Dog:
  latin = 'canis'
  def __init__(self, colour = 'brown'):
    self.colour = colour
    Dog.latin += colour
 
first = Dog()
second = Dog('red')
third = Dog('white')
print(second.latin)

