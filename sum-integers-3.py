#!/usr/bin/env python3

import sys
args = sys.argv[1:]
i = 0
j = 0
total = 0
while j < len(args):
    args_1 = args[j]
    with open(args_1, "r") as f:
        a = "".join(f.readlines()).rstrip("\n")
        a = a.split("\n")

    while i < len(a):
        if not ("a" <= a[i] and "z" >= a[i]) and a[i] != "" and a[i] != " ":
            total = total + int(a[i])
        i = i + 1
    i = 0
    a = []
    j = j + 1
print(total)
