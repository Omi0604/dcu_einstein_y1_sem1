#!/usr/bin/env python3

import sys

word = sys.stdin.readlines()

i = 0
while i < len(word):
    words = word[i].split("/")
    print(words[-1].rstrip())
    i = i + 1
