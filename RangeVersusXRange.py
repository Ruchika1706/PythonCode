#Range Function gives a list of integer numbers
#Range function only works for interger values
r1 = range(10)
print(r1)

#Loop through output of Range
for each in range(10):
    print(each)

#a range of numbers from 5 till 10 excluding 10
r2 = range(5,10)
print(r2)

#range(startValue, endValue, step)
#Range including step value, 5 to 11 at a step of 2 excluding upper limit
r3 = range(5,11,2)
print(r3)

r4 = range(-5,-11,-2)
print(r4)

r5 = range(11,5,-2)
print(r5)

#Both Range and XRange generates a list of integers. range returns python list object. xrange returns xrange object.
#XRange does not generate a static list at run time like range does. it creates value as you need them using yield .
#This type of object is known as generators.
generator = (x+x for x in range(3))
print(generator)

for each in generator:
    print(each)

#Generator is iterable , it is no collection thus has no length
#Collection keeps all values in memory and can access whenever needed
#Generator is useful for memory intensive tasks -> Calculate on fly and forget
#Generator are iterators but you can iterate over them once.
def hold_client(name):
    yield 'Hello, %s! You will be connected soon' % name
    yield 'Dear %s, could you please wait a bit.' % name
    yield 'Sorry %s, we will play a nice music for you!' % name
    yield '%s, your call is extremely important to us!' % name

for each in hold_client("Ruchika"):
    print(each)

mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)
# second time iteration on generator wont yield any result
for i in mygenerator:
    print(i)

#Yield is a keyword that is used like return, except that the function will return a generator
def createGenerator():
    mylist = range(5)
    for i in mylist:
        yield i*i
print("---------")
mygenerator = createGenerator()
for i in mygenerator:
    print(i)
#Wont be able to iterate the second time

for i in mygenerator:
    print(i)