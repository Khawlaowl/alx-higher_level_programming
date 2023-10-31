#!/usr/bin/python3
if number < 0:
    last = number % -10
else:
    last = number % 10
if last > 5:
    print("Last digit of {} is {}".format(number, last) + str1)
elif last == 0:
    print("Last digit of {} is {}".format(number, last) + str2)
else:
    print("Last digit of {} is {}".format(number, last) + str3)
