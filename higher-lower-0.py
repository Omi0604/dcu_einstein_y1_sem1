#!/usr/bin/env python3

p = int(input())

if p != 0:
    n = int(input())
    while n != 0:

        if n < p:
            print("lower")
            p = n
        elif n == p:
            print("equal")
            p = n
        elif n > p:
            print("higher")
            p = n
        n = int(input())
