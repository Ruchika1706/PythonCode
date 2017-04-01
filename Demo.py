#Simple Interest Calculator
principal = float(raw_input("Enter the principal amount for simple interest calculation \n"))
rate = float(raw_input("Enter the rate for simple interest calculation \n"))
time = float(raw_input("Enter the no of years for simple interest calculation \n"))
simple_interest = (principal*rate*time)/100
print(simple_interest)