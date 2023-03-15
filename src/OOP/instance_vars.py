'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


my_pet = Dog('Tedy', 2)
print(my_pet.__dict__)
my_pet.color = 'brown'
print(my_pet.__dict__)
del my_pet.name
print(my_pet.__dict__)
'''

class Dog:
    def __init__(self, name, age):
        self.__name = name
        self.age = age


my_pet = Dog('Tedy', 2)
print(my_pet.__dict__)
# print(my_pet.__name)

my_pet.__breed = 'Yorkie'
print(my_pet.__breed)