#Inheritance in OOP: Inheriting methods from one class to another class
class Students:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
    def getdata(self):
        self.name = raw_input("Enter your name");
        self.contact = raw_input("Enter your contact")
    def putdata(self):
        print("Your name is "+self.name)
        print("Your contact is"+ self.contact)


class ScienceStudent(Students):
    def __init__(self, age):
        self.age = age
    def science(self):
        print("I am a science student")

Rob = ScienceStudent(20)
Rob.science()
Rob.getdata()
Rob.putdata()