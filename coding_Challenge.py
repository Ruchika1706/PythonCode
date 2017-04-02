def student_discount(price):
    price = price -(0.1)*price
    return price

def regular_buyer_discount(amount):
    amount = amount - (0.05)*amount
    return amount

print(regular_buyer_discount(student_discount(100)))

#Calculate the value of mathematical expression x*(x+5)^2 where x= 5 using lambda expression.
print((lambda x: x * ((x + 5) ** 2))(5))

result = (lambda x: x*(x+5)**2)(5)
print(result)

#Consider a list in Python which includes prices of all the items in a store.
#Build a function to discount the price of all the products by 10%.
#Use map to apply the function to all the elements of the list so that all the product prices are discounted.

def discount(x):
    return (x - (0.1)*x)

newlist = [10,20,30,40]
print(list(map(discount,newlist)))