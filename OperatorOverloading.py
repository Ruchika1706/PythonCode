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
