#!/usr/bin/env python3

i = 0
p = int(input())
n = 0

while i < 5:
    n = int(input())

    if n < p:
        print("lower")
        p = n
    elif n == p:
        print("equal")
        p = n
    elif n > p:
        print("higher")
        p = n
    i = i + 1
