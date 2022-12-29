'''import scapy.all as scapy
request=scapy.ARP()'''
'''import scapy.all as scapy
request=scapy.ARP()
print(request.summary())
import scapy.all as scapy
request=scapy.ARP()
print(request.show())'''

'''from scapy.all import 
ip= IP()
print(ip)
print(ip.show())'''

from scapy.all import *
my_frame=Ether() /TCP()
print(my_frame)
print(my_frame.show())

from scapy.all import *
s=IP(dst="google.com")/ICMP()
print(s.show())



#print(my_frame.show())
#import pexpect
#print(pexpect.run('echo hello'))