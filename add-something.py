#!/usr/bin/env python3

a = []

n = input()

while n != "end":
    s = int(n)
    a.append(s)
    n = input()

b = int(input())

i = 0
while i < len(a):
    print(b + a[i])
    i = i + 1
