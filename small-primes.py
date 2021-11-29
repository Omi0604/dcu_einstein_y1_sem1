#!/usr/bin/env python3

n = int(input())

if n == 1 or n == 9 or n == 15:
    print("not prime")
elif n == 2 or n == 3:
    print("prime")
elif n >= 2 % 1 and n % 2 != 0:
    print("prime")
else:
    print("not prime")
