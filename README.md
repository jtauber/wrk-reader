wrk-reader
==========

exploring how to read old Cakewalk WRK files

`hexdump.py` dumps a binary file as a textfile of hex bytes that can be
annotated.

`hexcmp.py` compares an annotated dump with the original binary file to make
sure it's still equivalent. Whitespace and anything between # and newline is
ignored so annotations can make use of this.

I've started taking notes on my finding in `notes.md`.
