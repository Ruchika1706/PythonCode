#Crawler visits the web page and captures all the links from it and stores it in a file
#Takes saved URLs, visits each one and captures all the links from this as well
#urllib is the libray having all functions related to URLs, urlopen opens a URL given as input
from urllib2 import urlopen
import re
#In Python 3, we use from urllib.request import urlopen

#output is HTML code
html = urlopen("https://www.wikipedia.org")

#but the output is not in human readable format, so we use html.read()
print(html.read())



