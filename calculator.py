"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.

https://github.com/Amanda-alm/lab11-AA-ST
Partner 1: Amanda Almeida
Partner 2: Spencer Treadway
"""
import math

def square_root(a): return math.sqrt(a) # raise ValueError if a < 0

def hypotenuse(a,b): return math.hypot(a,b) #can have neg nums


# First example
def add(a, b): 
    a + b
def subtract(a,b): return a - b

def multiply(a,b): return a * b

def divide(a, b): return b / a   # raise ZeroDivisionError if a == 0

def logarithm(a, b): return math.log(b, a) # use math library/raise ValueError

def exponent(a,b): return ab


