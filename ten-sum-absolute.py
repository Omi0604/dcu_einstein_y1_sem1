#!/usr/bin/env python3

i = 0
n = 10
total = 0

while i < n:
    p = int(input())
    a = (p ** 2) ** 0.5
    total = total + a
    i = i + 1
    total = int(total)

print(total)
