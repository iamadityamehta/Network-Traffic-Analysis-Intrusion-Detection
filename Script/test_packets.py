from scapy.all import *

target = "192.168.1.12"

for port in range(1,50):
    pkt = Ether()/IP(dst=target)/TCP(dport=port,flags="S")
    sendp(pkt, iface="eth0")
