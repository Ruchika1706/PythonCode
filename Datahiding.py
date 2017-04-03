#Encapsulation and Data hiding in Python
#Usage of __ in front of the variable name to make it private and not accessible outside the class
class Myclass:
    __hiddenvariable = 0
    def add(self, increment):
        self.__hiddenvariable += increment
        print(self.__hiddenvariable)


test = Myclass()
test.add(5)
print(test.__hiddenvariable)