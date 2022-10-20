# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 18:49:32 2022

@author: its ya boy
"""
#to find the distance between two points
import math

x1 = float(input("Enter the x co-ordinate of first point: "))

print(x1)

y1 = float(input("Enter the y co-ordinate of first point: "))

print(y1)

x2 = float(input("Enter the x co-ordinate of second point: "))
print(x2)

y2 = float(input("Enter the y co-ordinate of second point: "))

print(y2)

s1= x1-x2
s2= y1-y2

d = math.sqrt((s1*s1)+(s2*s2))

print("The distance between two points is: ", d)





