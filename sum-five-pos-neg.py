#!/usr/bin/env python3

total_1 = 0
total_2 = 0
i = 0

while i < 5:
    n = int(input())
    if n > 0:
        total_1 = total_1 + n
    elif n < 0:
        total_2 = total_2 + n

    i = i + 1

print(total_2, total_1)
