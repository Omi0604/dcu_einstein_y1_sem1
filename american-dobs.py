#!/usr/bin/env python3

with open("irish-dobs.txt") as f:
   lines = f.readlines()

i = 0
while i < len(lines):
   t = lines[i].split()
   date = t[0].split("/")
   tmp = date[0]
   date[0] = date[1]
   date[1] = tmp
   t[0] = "/".join(date)
   lines[i] = " ".join(t)
   i = i + 1

with open("american-dobs.txt", "w") as f:
   output = "\n".join(lines) + "\n"
   f.write(output)
