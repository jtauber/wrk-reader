All files begin with

    43 41 4B 45 57 41 4C 4B

which is "CAKEWALK".

Next there is a 110-octet sequence that is mostly identical. The common parts are:

    1A 00 02 0A 02 00 00 00
    78 00 03 59 00 00 00 00
    00 00 00 00 00 00 00 ..
    .. 00 00 00 00 00 00 00
    00 01 01 00 00 00 00 00
    00 00 00 00 00 00 00 01
    01 01 FF FF 01 7F 00 00
    00 00 00 00 00 00 00 00
    00 00 00 00 00 00 00 00
    00 .. 20 40 80 00 00 00
    00 00 00 00 00 00 00 00
    .. .. 00 00 FE 00 00 00
    00 00 00 00 00 00 00 00
    16 16 00 00 00 03

Next are three strings, each proceeded by an incrementing byte then the length:

    00 06
    4D 43 49 43 6D 64

"MCICmd"
    
    01 04
    57 61 76 65

"Wave"
    
    02 04
    54 65 78 74

"Text"

What follows is always:

    03 0F

but it isn't clear if that's following the same pattern.

What follows that is a 100-200 octet sequence I haven't explored much yet.

## Notes Block

00 0E 04 00
00 00 01 00 00 00 0C 04 00 00 00 01 00 04 00

01 09 00 00 00
01 00 00 00 01 0C
00 00 04 02 3C 00 00 00 01 
