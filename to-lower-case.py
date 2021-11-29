#!/usr/bin/env python3

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"

s = input()

while s != "end":
    a = ""
    i = 0
    while i < len(s):
        if "A" <= s[i] and s[i] <= "Z":
            j = 0
            while s[i] != upper[j]:
                j = j + 1
            a = a + (lower[j])
        else:
            a = a + s[i]
        i = i + 1

    print(a)
    s = input()
