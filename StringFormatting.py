#Usage of String format()
numbers = [4,5,6]
newstring = "Numbers: {0},{1},{2}".format(numbers[0],numbers[1],numbers[2])
print newstring

#Display Dates
dates = [1,4,2017]
newstring = "Date is: {0}/{1}/{2}".format(dates[0],dates[1],dates[2])
print newstring

#this way the order of arguments can be changed
a = "{x}/{y}/{z}".format(z=2017,x=1,y=4)
print a