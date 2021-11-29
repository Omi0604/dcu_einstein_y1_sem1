#!/usr/bin/env python3

a = []
b = []
p = 0
j = 0

s = input()
while s != "end":
    s2 = s[9:]
    b.append(s2)
    s = s[6:8] + s[3:5] + s[0:2]
    a.append(s)
    s = input()

i = 0
while i < len(a):
    p = i
    j = i
    while j < len(a):
        if a[j] < a[p]:
            p = j
        j = j + 1
    tmp = a[p]
    a[p] = a[i]
    a[i] = tmp

    tmp2 = b[p]
    b[p] = b[i]
    b[i] = tmp2
    i = i + 1

i = 0
while i < (len(a) and len(b)):
    print(b[i])
    i = i + 1
