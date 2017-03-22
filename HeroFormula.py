#Triangle Area Calculation using Hero's Formula
side1 = float(raw_input("Enter first side of triangle"))
side2 = float(raw_input("Enter second side of triangle"))
side3 = float(raw_input("Enter third side of triangle"))
s = (side1 +side2 + side3)/2
area = (s*(s-side1)*(s-side2)*(s-side3))**0.5
print("Area of Triangle {0}",area)
