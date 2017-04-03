#Using the concept of object oriented programming and inheritance, create a super class named Computer,
# which has two sub classes named Desktop and Laptop.
#Define two methods in the Computer class named getspecs and displayspecs, to get the specifications and
# display the specifications of the computer.
#You can use any specifications which you want.
#The Desktop class and the Laptop class should have one specification which is exclusive to them for example
#  laptop can have weight as a special specification.
#Make sure that the sub classes have their own methods to get and display their special specification.
#Create an object of laptop/ desktop and make sure to call all the methods from the computer class
#  as well as the methods from the own class

class Computer:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    def getspecs(self):
        self.name = raw_input("Enter the name of computer")
        self.model = raw_input("Enter the model of computer")

    def displayspecs(self):
        print(self.name + " " +self.model)



class Laptop(Computer):
    def __init__(self, weight):
        self.weight = weight
    def getweight(self):
        self.weight = int(raw_input("Etner weight"))
    def putweight(self):
        print(self.weight)

class Desktop(Computer):
    pass