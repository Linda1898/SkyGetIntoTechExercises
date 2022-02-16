# Parentheses, Exponents, Multiplication and Division (left to right), Addition and Subtraction (left to right).
# from math import pi, tan, cos

import math
degrees = 80
radian = degrees * (math.pi/180)
horizontal_dist = 0.5
accel_gravity = 9.81
height_barrel = 1
velocity = 44
theta = radian

part_1 = height_barrel + horizontal_dist * math.tan(theta)
part_2 = accel_gravity * horizontal_dist ** 2
part_3 = 2 * (velocity * math.cos(theta)) ** 2
y = part_1-part_2/part_3
print(y)
print("The height of the projectile from the gun is", round(y,2))
