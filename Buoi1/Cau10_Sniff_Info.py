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
            payload = packet[Raw].load.decode('utf-8', errors='ignore')
            print(f"data: {payload}")

sniff(iface="Wi-Fi", filter="tcp and port 80", prn=packet_callback, store=0)