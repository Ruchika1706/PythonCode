import math
#Area of Rectangle
length = 3
breadth = 4
area_rectangle = length*breadth
print("Area of Rectangle is ",area_rectangle)
side = 5
area_square = side *side
print("Area of Square is ",area_square)
radius = 5
area_circle = math.pi*math.pow(radius,2)
perimeter = 2 * math.pi *radius
print("Area of Circle", area_circle)
print("Perimeter of Circle", perimeter)
base = 2
height = 4
area_triangle = (base *height)/2;
print("Area of Triangle",area_triangle)

#Square root of a number
number = 16
sq_root = number ** 0.5
print("Sqaure root of number is",(sq_root))

#Swap two variables
a = 5
b = 10
a,b = b,a
print("a=",a)
print("b=",b)