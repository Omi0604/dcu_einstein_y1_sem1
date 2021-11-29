#!/usr/bin/env python3

a = []
b = []

s = input()

while s != "end":
    n = int(s)
    if n % 2 == 1:
        a.append(n)
    else:
        print(n)
    s = input()

i = 0
while i < len(a):
    print(a[i])
    i = i + 1
