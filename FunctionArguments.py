#Passing arguments to the function, function to add two numbers
def add(num1,num2):
    print (num1+num2)

add(3,4)
add(100,200)

#making function return values
def add_1(num1,num2):
    c = num1+ num2
    d = num1- num2
    return c,d
x,y = add_1(6,5)
print x,y