class overloading:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __add__(self,other):
        a = self.a + other.a
        b = self.b + other.b
        print a
        print b
    def __str__(self):
        print(self.a)
        print(self.b)
test = overloading(3,4)
drive = overloading(5,6)
manual = test+drive

#Operator Overloading : Overload a particular operator to work with different data types
#Add coordinates of two places (x1,y1) and (x2,y2)
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getitem(self):
        self.x = int(raw_input("Enter the value of x coorindate"))
        self.y = int(raw_input("Enter the value of y coorindate"))

    def putitem(self):
        print("(x,y)"+"("+self.x+","+self.y+")")

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)

    def __sub__(self,other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

a1 = Point(3,4)
a2 = Point(5,6)
print(a1 + a2)