#!/usr/bin/env python3

n = input()
total = 0
i = 0
j = 0
while i < len(n):
    while i < len(n) and n[i] != "+":
        i = i + 1
    total = total + int(n[j:i])

    i = i + 1
    j = i

print(total)
