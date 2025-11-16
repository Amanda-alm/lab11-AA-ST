"""https://github.com/Amanda-alm/lab11-AA-ST
Partner 1: Amanda Almeida
Partner 2: Spencer Treadway
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.


"""
import math

def add(a, b): 
    return a + b
def square_root(a): return math.sqrt(a) # raise ValueError if a < 0

def hypotenuse(a,b): return math.hypot(a,b) #can have neg nums

# First example
def add(a, b): 
    a + b
def subtract(a,b): return a - b

def multiply(a,b): return a * b

def logarithm(a, b): return math.log(b, a) # use math library/raise ValueError

def exponent(a,b): return a ** b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError()
    return b / a

def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("log(a, b) requires a > 0 and b > 0")
    if a == 1:
        raise ValueError("log base 1 is undefined")
    return math.log(b) / math.log(a)

def exp(a, b):
    return a ** b