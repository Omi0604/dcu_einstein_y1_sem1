#!/usr/bin/env python3

i = 0
while i < 10:
    s = input()
    j = 0
    while j < len(s) and ("0" <= s[j] and s[j] <= "9"):
        j = j + 1
    print(int(s[:j]) + int(s[j:]))
    i = i + 1
