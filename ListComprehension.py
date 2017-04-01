# Create a list that contains squares of numbers from 0 to 4
list = [x*x for x in range(5)]
print list

#Alternative Way
# Create a list that contains squares of numbers from 0 to 4
list = [x**2 for x in range(5)]
print list

# Create a list that contains squares of numbers from 0 to 4 having only even numbers
list = [x**2 for x in range(5) if x**2 %2 == 0]
print list