#!/usr/bin/python3

# Use a single loop to iterate from 0 to 99
for num in range(100):
    # Use f-strings to format and print numbers with two digits
    print(f"{num:02d}", end=', ' if num < 99 else '\n')
