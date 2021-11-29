#!/usr/bin/env python3

total = 0
n = int(input())
m = int(input())

date = ((n - 1) * 30 + (m - 1))
print((date % 7) + 1)
