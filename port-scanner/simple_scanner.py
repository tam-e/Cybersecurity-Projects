# simple_scanner.py
import socket
import sys

def scan_port(host, port):
    """
    Attempts to connect to a specific port on the given host.
    """
    try:
        # Create a socket object (AF_INET for IPv4, SOCK_STREAM for TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a short timeout so the script doesn't hang forever
        s.settimeout(1) 
        
        # Attempt to connect to the host and port
        result = s.connect_ex((host, port))
        
        if result == 0:
            return True # Port is open
        else:
            return False # Port is closed or filtered
            
        s.close()

    except socket.gaierror:
        # Hostname resolution failed (e.g., bad URL)
        print(f"[-] Hostname could not be resolved: {host}")
        sys.exit()
    except socket.error:
        # General socket error
        print(f"[-] Could not connect to server: {host}")
        sys.exit()


def run_scanner():
    print("\n--- Simple TCP Port Scanner ---")
    
    # 1. Get the target host from the user
    target_host = input("Enter the target IP or hostname (e.g., example.com): ")
    
    # Define a list of common ports to scan
    common_ports = [21, 22, 23, 80, 443, 3389] 
    
    print(f"\nScanning common ports on: {target_host}...")
    
    # 2. Iterate (loop) through the ports and call the scan_port function
    for port in common_ports:
        if scan_port(target_host, port):
            print(f"[*] Port {port}: OPEN")
        else:
            print(f"[-] Port {port}: Closed")

# Execute the main function
if __name__ == "__main__":
    run_scanner()