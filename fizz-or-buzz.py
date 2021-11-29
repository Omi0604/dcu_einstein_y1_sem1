#!/usr/bin/env python3

a = int(input())

b = a % 3
c = a % 5


if b == 0 and c == 0:
    print("fizz-buzz")
elif b == 0:
    print("fizz")
elif c == 0:
    print("buzz")
else:
    print(a)
