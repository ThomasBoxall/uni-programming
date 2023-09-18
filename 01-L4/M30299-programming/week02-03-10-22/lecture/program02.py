# square first number and add to square of second number
# then find the square root
# this is pythagorous

import math

x = eval(input("Enter the x coordinate: "))
y = eval(input("Enter the y coordinate: "))

total = (x*x) + (y*y)

squareRoot = math.sqrt(total)

print("The third side of the triangle (z) is: ",squareRoot)