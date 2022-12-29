#socket is a package ,by this we can access host name or ip address
import socket
import subprocess
import sys
from datetime import datetime
subprocess.call('clear',shell=True)
remoteserver=input("enter a remote host to scan:")
remoteserverIP=socket.gethostbyname(remoteserver)
print("_"*60)
print("please wait,scanning remote host",remoteserverIP)
print("_" *60)
t1=datetime.now()
try:
    for port in range (1,5000):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result=sock.connect_ex((remoteserverIP,port))
        if result==0:
            print("port {}:  open".format(port))
            sock.close()
except KeyboardInterrupt:
    print("you pressed ctrl+c")
    sys.exit()
except socket.gaierror:
    print("hostname could not be resolved.existing")
    sys.exit()
except socket.error:
    print("couldn't connect the server")
    sys.exit()