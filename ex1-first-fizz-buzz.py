#!/usr/bin/env python3

a = int(input())

while not (a % 3 == 0 and a % 5 == 0):
    a = int(input())

print(a)
