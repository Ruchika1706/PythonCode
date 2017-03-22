#Conversion of a decimal number to hexdecimal
number = int(raw_input("Enter a decimal number"))
print("Value in hexdecimal number {0}".format(hex(number)))

#conversion of a decimal number to binary
print("Value in binary {0}".format(bin(number)))

#conversion of a decimal number to octal
print("Value in Octal {0}".format(oct(number)))

#conversion back to the decimal number from hexadecimal
print("Value in decimal of hexdecimal number {0}".format(int(hex(number),16)))

#conversion back to the decimal number from octal
print("Value in decimal of Octal number {0}".format(int(oct(number),8)))

#conversion back to the decimal number from binary
print("Value in decimal of Decimal number {0}".format(int(bin(number),2)))