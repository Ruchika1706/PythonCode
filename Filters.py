#Filters are used along with Lambda function to filter out certain elements from a list
new_list = [10,20,21,31,40,51]
#Filter out only even numbers present in the given list.
result = list(filter(lambda x: x % 2 == 0, new_list))
print result