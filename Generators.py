#Generators are type of iterables like list or tuple
#Generators can not be indexed like list but iterated over by using for loop
#Indexing in list allows modification of elements
#Generators can be created by functions or by using yield statements
#Say we want generators from range 0 to 4, generators used for generting numbers we can use in our code
def function():
    counter = 0
    while counter <= 4:
        yield counter
        counter += 1

for x in function():
    print(x)

#Second example: Generate a list of even numbers in a given range
def even_numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(even_numbers(10)))