#!/usr/bin/env python3

import sys

with open(sys.argv[1], "rb") as f:
    data = f.read()
    for ch in data:
        print("{:02X}".format(ch), end=" ")
print()
