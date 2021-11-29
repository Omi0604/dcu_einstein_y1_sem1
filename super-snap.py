#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()

dict = {}

i = 0
while i < len(s):
    word =  s.rstrip()
    if word not in dict:
        dict[word] = True
        print(dict[word])
    i = i + 1

