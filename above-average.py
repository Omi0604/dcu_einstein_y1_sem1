#!/usr/bin/env python3

a = []
s = input()
total = 0

while s != "end":
    a.append(s)
    total = total + int(s)
    s = input()

i = 0
while i < len(a):
    if int(a[i]) > total // len(a):
        print(a[i])
    i = i + 1
