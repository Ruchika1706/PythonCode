number1 = int(raw_input("Enter first number"))
number2 = int(raw_input("Enter Second number"))
number3 = int(raw_input("Enter Third number"))
if((number1 >= number2) and (number1 >= number3)):
    print("{0} is largest".format(number1))
elif ((number2 >= number1) and (number2 >= number3)):
    print("{0} is largest".format(number2))
else:
    print("{0} is largest".format(number3))