#Open a file
file = open("Sample.txt",'rw')
#do something with the file, Read the file
content = file.read(10) # argument is the no of bytes you want to read
print(content)
file.close()

file = open("Sample.txt",'rw')
content1 = file.readline() # reads only first line
print(content1)
file.close()

#Writing to the file, this will over write the file contents if the file exists, use append mode
file = open("Sample.txt",'w')
file.write('This is the text i want to write hellloooo\n')
file.close()

#Open a file
file = open("Sample.txt",'rw')
#do something with the file, Read the file
content = file.read() # argument is the no of bytes you want to read
print(content)
file.close()





