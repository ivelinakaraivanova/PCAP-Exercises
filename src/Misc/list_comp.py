# numbers = [i for i in range(1, 100)]

# numbers = [i for i in range(1, 100) if i % 3 == 0]

# numbers = [0 if i % 2 == 0 else 1 for i in range(100)]

# table = [[i for i in range(1, 6)] for j in range(5)]

# print(table)

print(list(map(lambda i: i*2, [1,2,3,4,5])))
print(list(filter(lambda i: i % 2 == 0, [1, 2, 3, 4, 5])))