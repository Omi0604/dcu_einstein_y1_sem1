#!/usr/bin/env python3

import sys
total = 0

args = sys.argv[1:]

i = 0
while i < len(args):
    with open(args[i]) as f:
        s = f.read().split()
    j = 0
    while j < len(s):
        total = total + int(s[j])
        j = j + 1
    i = i + 1

print(total)
