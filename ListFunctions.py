fruits = [ "Apple", "Mango", "Orango", "Banana"]
#add en element to the list at the end
fruits.append("Peach")
print(fruits)

print(len(fruits))

#insert function particular item at particular position
fruits.insert(1,"Peach")
print(fruits)


#index of item
print(fruits.index("Banana"))
#if item not in list, ValueError
print(fruits.index("Banasssna"))


