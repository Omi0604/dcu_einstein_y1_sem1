#!/usr/bin/env python3

n = 10
i = 0
smallest = int(input())

while i < n - 1:
    v = int(input())
    if smallest > v and v > 0:
        smallest = v
    i = i + 1

print(smallest)
