#Class is a classification of a particular thing
# __func__ dunders or double underscore methods
class Students:
    def __init__(self,name, contact):
        self.name = name
        self.contact = contact


#define methods of the class, get input from the user
    def getdata(self):
        print("Accepting Data")
        self.name = raw_input("Enter your name")
        self.contact = raw_input("Enter your phone number")

    def putdata(self):
        print(self.name)
        print(self.contact)


#Creating Objects of a class
John = Students("blank",0)
John.getdata()
John.putdata()
