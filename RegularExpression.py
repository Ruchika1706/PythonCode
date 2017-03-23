import re

line = "Miser"
line1 = "Missisippi"

matchObj = re.match( r'.*is',line)
matchObj1 = re.match( r'.*is',line1)
matchObj2 = re.match( r'.*?is',line1)
print "matchObj.group() : ", matchObj.group()
print "matchObj1.group() : ", matchObj1.group()
print "matchObj2.group() : ", matchObj2.group()

