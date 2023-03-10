import random

# print(random.random())
# print(random.random())
# print(random.random())


# random.seed(0)
# print(random.random())
# print(random.random())
# print(random.random())


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ['Lily', 'Mary', 'Dina', 'Jo', 'Mark', 'Jino']


# print(random.choice(numbers)) # numbers can be repeated
# print(random.choice(names))
# print(random.choice('names'))

print(random.sample(names, 3)) # always unique names