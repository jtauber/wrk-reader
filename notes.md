All files begin with

    43 41 4B 45 57 41 4C 4B

which is "CAKEWALK".

Next there is a 110-octet sequence that is mostly identical. The common parts
are:

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

I'm not sure what indicates the exact start of a block of notes on a track,
but at some point there is a word indicating the number of notes on a track:

    00 07

followed by an eight-byte sequence for each note:

    00 06 00 00 90 30 40 3A
    00 7C 00 00 90 28 40 46
    00 EE 00 00 90 2D 40 98
    00 A4 01 00 90 2D 40 24
    00 D6 01 00 90 29 40 34
    00 58 02 00 90 26 40 34
    00 D0 02 00 90 2B 40 94

The first four-bytes seem to be a little-endian double word indicating the
time offset. The fifth byte is always `90` which likely corresponds to the
MIDI command for `NOTE ON`. What follows is likely the pitch value, velocity
and duration of the note.
