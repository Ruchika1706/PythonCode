#Functional programming is when you write code in a particular fashion
def add_ten(x):
    return x+10
#call any function twice
def twice(func, arg):
    return func(func(arg))

print(twice(add_ten, 4))