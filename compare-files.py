#!/usr/bin/env python3

import sys
args = sys.argv[1:]

with open(args[0]) as f:
    s = f.read()

with open(args[1]) as f:
    t = f.read()

i = 0
while i < len(t) and i < len(s) and s[i] == t[i]:
    i = i + 1

if i < len(t) or i < len(s):
    s = s[0:i]
    lines = s.split("\n")
    print(len(lines) - 1, len(lines[len(lines) - 1]))
