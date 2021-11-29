#!/usr/bin/env python3

total = 0
i = 0
n = int(input())

while n != 0:

    if n > 0:
        total = total + n
    elif n < 0:
        total = total + (n * -1)
    n = int(input())
    i = i + 1

print(total)
