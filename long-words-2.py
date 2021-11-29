#!/usr/bin/env python3

if __name__ == "__main__":
  a = ["dog", "mouse", "cat", "gorilla"]

b = []
i = 0
while i < len(a) and len(a[i]) < 6:
  i = i + 1
if i < len(a):
  print(a[i])
