#!/usr/bin/env python3

total_1 = 0
total_2 = 0

n = int(input())

while n != 0:
    if n > 0:
        total_1 = total_1 + n
    elif n < 0:
        total_2 = total_2 + n
    n = int(input())

print(total_2, total_1)
