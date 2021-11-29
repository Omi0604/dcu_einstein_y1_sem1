#!/usr/bin/env python3

import sys

nums = {
    "one": "eins",
    "two": "zwei",
    "three": "drei",
    "four": "vier",
    "five": "funf",
    "six": "sechs",
    "seven": "sieben",
    "eight": "acht",
    "nine": "neun",
    "ten": "zehn",
}

number = sys.stdin.readlines()
i = 0
while i < len(number):
    print(nums[number[i].rstrip()])
    i = i + 1
