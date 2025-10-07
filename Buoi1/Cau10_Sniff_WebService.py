from scapy.all import *
pcap_file = "web_service_capture.pcap"
packet_writer = PcapWriter(pcap_file, append=True, sync=True)
def process_packet(packet):
    packet_writer.write(packet)

sniff(iface="Wi-Fi", filter="tcp and port 80", prn=process_packet, store=0)