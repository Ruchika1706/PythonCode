def square(x):
    return x**2

print(square(4))

#Lambdas are called Anonymous functions. Lambdas do not have return statements
#Lambdas can be used anywhere and you do not need to assign it to particular variable
# Alternative using Lamdas
result = (lambda x: x**2)(30)
print(result)

#Alternative without using lambda
print((lambda x: x**2)(30))