#!/usr/bin/python3

# Start with the ASCII code for 'a'
for char_code in range(ord('a'), ord('z') + 1):
    if char_code not in (ord('q'), ord('e')):
        print(chr(char_code), end='')
