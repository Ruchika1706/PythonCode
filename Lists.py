names = [ "Ruchika", "Jyoti", "Shashi"]
print(names[0])
print(names[1])
print(names[2])
print(names)

numbers = [1,2,3,4,5,6]
print(numbers)
print(numbers[4])


abc = []
print(abc)


numbers = [1,1,1,1,1,1]
#insert element in list at specific index
numbers[2]=3
print numbers

#add lists
new_numbers = [2,2,2,2,2]
print(numbers + new_numbers)
print(numbers *3)

fruits = ["Apple", "Mango", "Peach"]
print("Apple" in fruits)
if "Apple" in fruits:
    print("Apple is present")