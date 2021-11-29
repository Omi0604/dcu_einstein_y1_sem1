#!/usr/bin/env python3

import sys
n = int(sys.argv[1])
s = input()
start = 0
i = 0
while i < n:
    while start < len(s) and s[start] != ",":
        start = start + 1
    start = start + 1
    i = i + 1
end = start
while end < len(s) and s[end] != ",":
    end = end + 1
print(s[start:end])
