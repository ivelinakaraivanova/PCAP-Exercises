'''
def greet(text):

    def print_greet():
        print(text)

    return print_greet

say_hello = greet('Hello')
say_hello()
'''
 # a function defined inside another function that remembers the values of the outer function

def make_multiply_closure(x):

    def multiply(y):
        return x*y
    
    return multiply

multiply_5 = make_multiply_closure(5)
multiply_12 = make_multiply_closure(12)

print(multiply_5(10))
print(multiply_5(20))

print(multiply_12(10))
print(multiply_12(20))
