#Filters are used along with Lambda function to filter out certain elements from a list
new_list = [10,20,21,31,40,51]
result = list(filter(lambda x: x % 2 == 0, new_list))
print result