#!/usr/bin/python3
# Define variables a and b
a = 10
b = 5

# Import the required functions from calculator_1.py
from calculator_1 import add, sub, mul, div

# Perform calculations and print the results
result_add = add(a, b)
result_sub = sub(a, b)
result_mul = mul(a, b)
result_div = div(a, b)

# Print the results in the specified format
print(f"{a} + {b} = {result_add}")
print(f"{a} - {b} = {result_sub}")
print(f"{a} * {b} = {result_mul}")
print(f"{a} / {b} = {result_div}")
