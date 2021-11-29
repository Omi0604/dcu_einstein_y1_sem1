#!/usr/bin/env python3

s = input()
while s != "end":
    tokens = s.split()
    s = input()
    print(" ".join(tokens[5:]))
