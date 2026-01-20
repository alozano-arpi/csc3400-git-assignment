import math 

# addition
def add(n1, n2):
    return n1 + n2

# subtraction
def sub(n1, n2):
    return n1 - n2

# multiplication
def multiply(n1, n2):
    return n1 * n2

# division
def divide(n1, n2):
    if n2 == 0:
        return "ERROR: Cannot divide by zero"
    return n1 / n2

# power
def power(n1, n2):
    return n1**n2

# square root
def square(n1, n2):
    if n1 < 0:
        return "Cannot take square root of negative number"
    return math.sqrt(n1)