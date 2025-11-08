# analyzer.py
from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    """
    This function is called for every packet captured.
    It analyzes the packet and prints key details.
    """
    # Check if the packet has an IP layer (most network traffic does)
    if IP in packet:
        # Extract Source and Destination IP addresses
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "UNKNOWN"
        
        # Check for common protocols
        if TCP in packet:
            protocol = "TCP"
            # We can also check ports for common services
            service = f" (Src Port: {packet[TCP].sport} -> Dst Port: {packet[TCP].dport})"
        elif UDP in packet:
            protocol = "UDP"
            service = f" (Src Port: {packet[UDP].sport} -> Dst Port: {packet[UDP].dport})"
        elif ICMP in packet:
            protocol = "ICMP"
            service = "" # ICMP doesn't use ports
        else:
            service = ""

        # Print the extracted information
        print(f"[*] {protocol}: {src_ip} -> {dst_ip}{service}")


def run_analyzer():
    print("\n--- Simple Packet Analyzer (Capturing 5 packets) ---")
    print("Press Ctrl+C to stop early.")
    
    # The sniff function captures packets
    # prn=packet_callback: calls our function for each packet
    # count=5: limits the capture to 5 packets for a quick test
    # filter="ip": only capture packets with an IP layer
    
    sniff(prn=packet_callback, count=5, filter="ip")
    
    print("\n--- Capture Finished ---")


# Execute the main function
if __name__ == "__main__":
    try:
        run_analyzer()
    except PermissionError:
        print("\n[!!!] ERROR: Running Scapy often requires elevated permissions.")
        print("Run your terminal (or VS Code) as Administrator/root to capture traffic.")
    except Exception as e:
        print(f"\n[!!!] An unexpected error occurred: {e}")