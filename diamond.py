#!/usr/bin/env python3

import sys

n = int(sys.argv[1])

i = 1
# i < len(n)

while i <= n:
    print(" " * ((n - i) // 2) + "*" * i)
    i = i + 2

j = n - 2
while 0 < j:
    print(" " * ((n - j) // 2) + "*" * j)
    j = j - 2
