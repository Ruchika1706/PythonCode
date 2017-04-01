counter = 0
while counter<=10:
    print(counter)
    counter+=1

for each in range(5):
    print("I am a programmer")

#Task no 2: Create a function which displays out the square values of numbers from 1 to 9.
def square(num):
    print(num*num)

for each in range(1,10):
    square(each)

#Alternative and better way
def square():
    for each in range(1, 10):
        print(each*each)
square()
