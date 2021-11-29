#!/usr/bin/env python3

s = input()
prefix = ""
if s[0] == "-":
    prefix = "-"
    s = s[1:]

i = 0
while i < len(s) and s[i] != ".":
    i = i + 1

if i < len(s):
    integer = s[:i]
    fract = s[i + 1:]
else:
    integer = s
    fract = ""

if len(integer) == 0:
    integer = "0"

if len(fract) == 0:
    fract = "0"
print(prefix + integer + "." + fract)
