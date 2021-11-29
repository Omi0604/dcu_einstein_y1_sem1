#!/usr/bin/env python3

import sys
dict = {}

with open("translation.txt") as f:
    text = f.readline()
    while text:
        word = text.split()
        dict[word[0]] = word[1]
        text = f.readline()

number = sys.stdin.readlines()

i = 0
while i < len(number):
    print(dict[number[i].rstrip()])
    i = i + 1
