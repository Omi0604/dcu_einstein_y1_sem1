#!/usr/bin/env python3

s = input()
while s != "end":
    s = s.split()
    if s[2] != "1":
        print(" ".join(s))
    s = input()
