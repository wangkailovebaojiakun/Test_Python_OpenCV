#pack and unpack
#pack(fmt, v1,v2)
#unpack(fmt,string)
#calcsize(fmt)

from struct import *

a = 'hello'
b = 'world'
c = 255
d = 45.12
e = 0

fmt = '5s6sifi'
bytes = pack(fmt,a,b,c,d,e)
print 'a is',a,'-- b is',b,'-- c is',c,'-- d is',d,'-- e is',e
print 'fmt is ',fmt
print 'bytes is',bytes

# this will wrong with 
#struct.error: pack expected 1 items for packing (got 5)
#fmt = '!I'
#bytes = pack(fmt,a,b,c,d,e)
#print 'fmt is ',fmt
#print 'bytes is',bytes
a,b,c,d,e = unpack(fmt,bytes)
print a,b,c,d,e
