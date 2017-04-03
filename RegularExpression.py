#re.match(pattern,string) exact match
#re.search(pattern,string) searches for pattern in entire string
#re.findall(pattern,string) : list of all items which matched the pattern, len of list will give count of the occurences
#re.sub(pattern, replacement_string, string_where_search_and_replace). This returns a new string
# dot (.) metacharacter
#re.search() and re.match do not return Boolean Values, instead return objects
import re

line = "Miser"
line1 = "Missisippi"

matchObj = re.match( r'.*is',line)
matchObj1 = re.match( r'.*is',line1)
matchObj2 = re.match( r'.*?is',line1) # stop at the first match, not the greedy match for longest substring
print "matchObj.group() : ", matchObj.group()
print "matchObj1.group() : ", matchObj1.group()
print "matchObj2.group() : ", matchObj2.group()

#Regular Expressions in python
#Manipulate strings in python code, powerful tool for manipulating strings
#Strings matching a particular pattern, for example matching email address

#re.match() tries to find an exact match
pattern = r"eggs"   #'r' stands for raw string, string should contain eggs
if re.match(pattern, "eggseggsbacon"): #Match  found
    print('Match found')
else:
    print('no Match found')

if re.match(pattern, "baconeggseggs"): #Match  not found
    print('Match found')
else:
    print('no Match found')

if re.match(pattern, "bacon"):   #Match not found
    print('Match found')
else:
    print('no Match found')

if re.match(pattern, "baconeggsbacon"): #Match not found, even though pattern in present but not in beginning or end
    print('Match found')
else:
    print('no Match found')



if re.match(pattern, "baconeggseggsbacon"): #Match not found
    print('Match found')
else:
    print('no Match found')




#Substitution in a string, find and replace functionality
#search and findall functionality
#search() searches almost everwhere in the string
if re.search(pattern,"baconeggseggsbacon"): # pattern is searched almost everywhere in the string
    print("String searched")
else:
    print("String not found ")

#to count the number of patterns found in the string
if re.findall(pattern, "baconeggseggsbacon"):
    print("Match found")
else:
    print("Match not found ")

print(re.findall(pattern, "baconeggseggsbacon"))
print(len(re.findall(pattern, "baconeggseggsbacon")))

#find and replace functionality
string = "My name is John, hi I am John"
pattern = r"John"
re.search(pattern, string)

newstring = re.sub(pattern, "Ruchika", string)
print(newstring)

#the dot metacharacters, metacharacters allow you to make RE more powerful
pattern = r"gr.y"
if re.match(pattern, "grey"):
    print("Matched")

if re.match(pattern, "grAy"):
    print(" Matched")

#Caret ^ starting of string  and dollar $ ending of string  metacharacters
pattern = r"^Gr.y$"
if re.match(pattern, "GrEy"):
    print("Match 1")

# to match any number of characters we use *, in python we use (.*) group for the same
pattern = r"^Gr(.*)y$"
if re.match(pattern, "GrEeeeey"):
    print("Match 1")


