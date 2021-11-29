#!/usr/bin/env python3

n = int(input())
i = 0
while i < n:
    if i == 0:
        print(n * "*")
    elif 0 < i < n - 1:
        print("*" + ((n - 2) * " ") + "*")
    elif i == n - 1:
        print(n * "*")
    i = i + 1
