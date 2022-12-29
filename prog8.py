'''import ifaddr
adapters=ifaddr.get_adapters()
for adapter in adapters:
    print("IP of network adapter"+adapter.nice_name)
    for ip in adapter.ips:
        print("%s/%s"%(ip.ip,ip.network_prefix))'''


'''import ifaddr
adapters=ifaddr.get_adapters(include_unconfigured=True)
for adapter in adapters:
    print("IP of network adapter"+adapter.nice_name)
    if adapter.ips:
        for ip in adapter.ips:
            print("%s/%s"%(ip.ip,ip.network_prefix))
    else:
        print("No IPs configured")'''

import psutil
#result01=psutil.cpu_times()
#result02=psutil.cpu_freq()
#result03=psutil.cpu_stats()
#result04=psutil.disk_partitions()
result05=psutil.net_io_counters()
#print(result01)
#print(result02)
#print(result03)
#print(result04)
print(result05)
#psutil
import psutil
network_stats=psutil.net_io_counters(pernic=False)
bytes_sent=getattr(network_stats,'bytes_sent')
bytes_recv=getattr(network_stats,'bytes_recv')
#print("Bytes sent ={0} | Bytes Recevied ={1}".format(bytes_sent,bytes_recv))