#!/usr/bin/env python3

n = int(input())
m = n % 100
n = n - m
p = n // 10000
q = (n - (p * 10000)) // 100

print((q * 10000) + (p * 100) + m)
