#!/usr/bin/env python3

j = 0
total = 0

while total != 1000:
    s = input()
    i = 0
    while i < len(s) and s[i] != "+":
        i = i + 1
    m = int(s[0:i])
    k = int(s[i + 1:])
    total = k + m
    print(k + m)
    j = j + 1
