#!/usr/bin/env python3

a = []

s = input()
while s != "end":
    a.append(s)
    s = input()

n = input()
i = 0
while i < len(a):
    s = a[i]
    if s[0] == n:
        print(s)
    i = i + 1
