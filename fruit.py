#!/usr/bin/env python3

import sys
word = sys.stdin.readlines()

fruit = {
    "apple": True,
    "pear": True,
    "orange": True,
    "banana": True,
    "cherry": True,
}

i = 0
while i < len(word):
    if word[i].rstrip() in fruit:
        sys.stdout.write(word[i])
    i = i + 1
