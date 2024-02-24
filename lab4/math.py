import math
#1
degree = int(input())
print(math.radians(degree))

#2
height,base1,base2 = map(int, input("Enter height, base1, and base2 separated by spaces: ").split())
area = (base1 + base2)/2 * height
print(area)

#3
sides = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
area = (sides * length ** 2) / (4 * math.tan(math.pi / sides))
print(int(area))

#4
base = int(input("Length of base: "))
height = int(input("Height of parallelogram: "))
area = base * height
print(area)