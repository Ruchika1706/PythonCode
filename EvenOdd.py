#Test if a given number is even or odd
number = int(raw_input("Enter a number"))
if (number % 2 == 0):
    print("{0} is Even".format(number))
else:
    print("{0} is Odd".format(number))