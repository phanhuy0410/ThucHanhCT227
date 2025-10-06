from scapy.all import *
from scapy.layers import http
def packet_callback(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host.decode() + \
            packet[http.HTTPRequest].Path.decode()
        print(f"\n[+] Tìm thấy HTTP Request: ")
        print("================================")
        print(f"URL: {url}")
        print("================================")
        if packet.haslayer(Raw):
            payload = packet[Raw].load.decode('utf-8', errors='ígnore')
            print(f"data: {payload}")

sniff(iface="Realtek 8821CE Wireless LAN 802.11ac PCI-E NIC", filter="tcp and port 80", prn=packet_callback, store=0)