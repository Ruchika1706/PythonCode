#join() join a string with a list
print(",".join(["Apple","Banana","Mango"]))
print(":".join(["Apple","Banana","Mango"]))
print("_hello_".join(["Apple","Banana","Mango"]))

#output
#Apple,Banana,Mango
#Apple:Banana:Mango

#replace()
print("Hello There!".replace('H','E'))
print("Hello There!".replace('There','World'))

#replace function does not change the actual value stored in the string.
newString = "Hello There"
print(newString.replace("There", "World"))
print(newString)

#determine if a string if present at start/end of string startsWith()
newString = "This is a string"
print(newString.startswith("This"))
print(newString.startswith("There"))
print(newString.endswith("string"))
print(newString.endswith("stri"))

#captialize function
print(newString.capitalize())

#uppercase function and lowercase function
print(newString.upper())
print(newString)
print(newString.lower())