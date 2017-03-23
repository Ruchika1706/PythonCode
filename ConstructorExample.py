#Question: While printing x, you want to mosify the behavior and print "Hello name" where name is argument to the constructor.
class Test:
    def __init__(self,name):
        self.name = name
        # str should return String return type
    def __str__(self):
        return("Hello "+ " " +self.name)
x = Test("Ruchika")
print x