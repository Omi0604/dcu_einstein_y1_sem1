#!/usr/bin/env python3

import sys

with open("translation.txt") as f:
   s = f.read()
   sys.stdout.write(s)
