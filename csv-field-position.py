#!/usr/bin/env python3

import sys

n = sys.argv[1]
s = input()

a = []

i = 0
while i < len(s):
   if s[i] == ",":
      a.append(s[:i])
      s = s[i + 1:]
      i = 0
   i = i + 1

a.append(s)

pos = -1
i = 0
while i < len(a) and pos == -1:
   if a[i] == n:
      pos = i
   i = i + 1

print(pos)
