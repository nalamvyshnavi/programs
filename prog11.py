#scapy is use to packet monitoring it gives the packet details
from scapy.all import *
a=IP(ttl=10)
print(a)
print(a.src)
a.dst="192.168.1.1"
print(a)
print(a.src)

del(a.ttl)
print(a.show())
b=IP()
print(b.show())

'''c=IP()/TCP()
print(c.show())
d=Ether()/IP()/TCP()
print(d.show())
e=IP()/TCP()/"GET /HTTP/1.0\r\n\r\n"
print(e.show())'''

#j=a=Ether()/IP(dst="www.slashdot.org")/TCP()/"GET/index.html HTTP/1.0 \n\n"
#print(hexdump(j))

k=IP(dst="www.slashdot.org/30")
dst=Net('www.slashdot.org/30')
print([p for p in k])