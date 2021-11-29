#!/usr/bin/env python3

import sys

file_name = "hello.txt"

with open("hello.txt", "w") as f:
    f.write("Hello world.\n")
