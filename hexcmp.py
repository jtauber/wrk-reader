#!/usr/bin/env python3

import sys

with open(sys.argv[1], "rb") as f:
    data = f.read()

    offset = 0
    with open(sys.argv[2]) as g:
        for line in g:
            for b in line.split("#")[0].strip().split():
                ch = int(b, 16)
                if data[offset] != ch:
                    print("mismatch at offset {} (expected {:02X} but got {:02X})".format(offset, data[offset], ch))
                    print(line)
                    break
                offset += 1
