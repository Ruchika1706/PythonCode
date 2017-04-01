#minimum function
print(min(3,4,1,2,4))


#maximum function
print(max(3,4,1,2,4))

#absolute value function: Core value without including sign of the value
print(abs(-203))

#products and their prices
product_list = {'car':900000, 'bike':700000,'cycle':10000,'scooty':45000,'auto':25000}
product = raw_input("Enter the product name")
if product in product_list:
    print(product_list.get(product,"Product found"))
else:
    print("product not found")

#List out  all the odd numbers from 1 to 100 using lists in Python.
list = [num for num in range(1,100) if num%2 != 0]
print list