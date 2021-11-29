#!/usr/bin/env python3

x = int(input())
y = ""

h = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "a", "b", "c", "d", "e", "f"]

while x != 0:
    y = h[(x % 16)] + y
    x = x // 16

print(y)
