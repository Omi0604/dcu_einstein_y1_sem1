#!/usr/bin/env python3

n = 10
i = 0
total = 0

while i < n:
    p = int(input())
    if p % 2 == 0:
        total = total + p
    i = i + 1

print(total)
