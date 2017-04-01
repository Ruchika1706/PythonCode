#Dictionary Data Structures: key: value pairs
test = {'name' :'Rohit','age':26}
print test
print test['name']
print test['age']

#list of dictionaries
first = [{'name' :'Ruchika','age':26}, {'name' :'Rohit','age':26}]
print(first)
print(first[0]['name'])
print(first[1]['age'])

#dictionary with key as integer
sample = { 1: "one", 2: "two", 3: "three"}
print sample
print sample[3]
print sample.get(3) # Alternative function present for dictionary
#If the key is not found, we can use the get() to print a message
print sample.get(3333,"Key not found")

#test if an element is present in dictionary's keys
print(1 in sample)
print(5 in sample)

#test for value present in dictionary.keys()
print(1 in sample.keys())
print("one" in sample.values())