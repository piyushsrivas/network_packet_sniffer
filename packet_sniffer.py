from scapy.all import sniff, IP, TCP, UDP, ICMP, conf

# Use L3 Socket for Windows
conf.L3socket

def analyze_packet(packet):
    print("\n---------------- PACKET CAPTURED ----------------")

    if packet.haslayer(IP):
        ip_layer = packet[IP]
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")

        if packet.haslayer(TCP):
            print("Protocol: TCP")
            print(f"Source Port: {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        elif packet.haslayer(UDP):
            print("Protocol: UDP")
            print(f"Source Port: {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        elif packet.haslayer(ICMP):
            print("Protocol: ICMP")

        if packet.haslayer("Raw"):
            print(f"Payload: {packet['Raw'].load}")
        else:
            print("Payload: None")

def start_sniffing():
    print("Starting packet sniffer... Press CTRL+C to stop.")
    sniff(prn=analyze_packet, store=False, filter="ip")

if __name__ == "__main__":
    start_sniffing()
