# print(chr(ord('a') + 2))
# print(ord('a'))
# print(chr(ord('a')))
# print(chr(ord('a') + 2))

'''
def a():
    hey = 5
 
    def b():
        print(hey)
 
    return b
 
x = a()
print(x())
'''

# print('20' > '8' or '20' > 8)
# print('20' > '8')

# print(float(1,0))

'''
class Art():
 masterpiece = 'John'
 def __init__(self):
  self.name = 'One'
 
print(len(Art().__dict__))
print(Art().__dict__)
'''

'''
class Sampl:
 def __init__(self, vala, valb=0):
  pass

obj = Sampl(5,4,3)
obj = Sampl(4,3)
obj = Sampl(3)
obj = Sampl(None)

print(obj)
'''

# inpt = ['Adam', 'Mary', 'Kate']
# res = ''.join(list(map(lambda x: x+'-', inpt)))
# print(res)

'''
class A:
 b = 1
 def __init__(self):
  self.c = 0
 
print(hasattr(A(), 'c'))
print(A().__dict__)
'''

'''
class X:
 Y = 1
 def __init__(self):
  self.z = 0
 
print(hasattr(X, 'z'))
print(X().__dict__)
'''

'''
class House:
 def __init__(self):
  self.rooms = 5
 
print(House())
'''

'''
def a():
    hey = 5
 
    def b():
        print(hey)
 
    return b
 
x = a()
print(x())
'''

'''
lst = [['*' for i in range(2)] for j in range(2)]
print(lst)
'''

'''
class X:
 Y = 1
 def __init__(self):
  self.z = 0
 
print(hasattr(X, 'z'))
'''

'''
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())
'''

'''
class Ex(Exception):
    def __init__(self, msg):
        super().__init__(msg+msg)
        self.args = (msg,)

try:
    raise Ex('ex')
except Ex as e:
    print(e)
except Exception as e:
    print(e)
'''

'''
class A:
    def __init__(self):
        pass

a = A(1)
print(hasattr(a, 'A'))
'''

class A:
    A = 1


print(hasattr(A, "A"))