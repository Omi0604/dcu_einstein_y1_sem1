#!/usr/bin/env python3

a = []
p = 0
j = 0

s = input()
while s != "end":
    a.append(int(s))
    s = input()

i = 0
while i < len(a):
    j = i
    p = i
    while j < len(a):
        if a[j] < a[p]:
            p = j
        j = j + 1
    tmp = a[p]
    a[p] = a[i]
    a[i] = tmp
    i = i + 1

print(a[len(a) // 2])
