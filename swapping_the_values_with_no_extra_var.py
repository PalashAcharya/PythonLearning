# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 18:16:36 2022

@author: PalashAcharya
"""


#swapping the values of variables 

a= int(input("Enter the value of the first number a : "))

print(a)

b= int(input("Enter the value of the second number b : "))

print(b)
 
b=a+b
a=b-a
b=b-a

print("Here is the swapped value of a :", a)

print("Here is the swapped value of b :", b)