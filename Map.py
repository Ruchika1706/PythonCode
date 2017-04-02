#Map performs operation, perform function  on given iterables like list
#Say you want to add 2 to all members in a list
def add(x):
    return x+2

new_list = [10,20,30,40,50]
print(list(map(add,new_list)))
print new_list

#Usage of Lambda and map together
new_list = [10,20,30,40,50]
print(list(map(lambda x:x+2,new_list)))

