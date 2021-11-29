#!/usr/bin/env python3

a = input()
b = input()
c = input()

p = len(a)
q = len(b)
r = len(c)

if p > r and p > q:
    print(a)
elif q > p and q > r:
    print(b)
else:
    print(c)
