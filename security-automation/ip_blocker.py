import re
from collections import Counter

# --- CONFIGURATION ---
# Change these lines to include the folder name
LOG_FILE = "security-automation/login_attempts.log"
BLOCK_LIST_FILE = "security-automation/blocked_ips.txt"
FAILED_THRESHOLD = 3

def analyze_logs():
    print(f"--- 🛡️ SECURITY AUTOMATION: ANALYZING {LOG_FILE} ---")
    
    failed_ips = []
    
    # Open and read the log file
    with open(LOG_FILE, "r") as file:
        for line in file:
            # Look for the "Failed password" pattern
            if "Failed password" in line:
                # Use Regex to extract the IP address at the end of the line
                ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
                if ip_match:
                    failed_ips.append(ip_match.group(1))

    # Count the occurrences of each IP
    ip_counts = Counter(failed_ips)
    
    # Identify and "block" IPs that exceed the threshold
    new_blocks = []
    for ip, count in ip_counts.items():
        if count >= FAILED_THRESHOLD:
            print(f"[⚠️ ALERT] {ip} has {count} failed attempts. BLOCKING...")
            new_blocks.append(ip)
    
    if new_blocks:
        write_blocks(new_blocks)
    else:
        print("[✅] No suspicious activity detected.")

def write_blocks(ips):
    # Save the blocked IPs to a separate file (simulating a firewall rule)
    with open(BLOCK_LIST_FILE, "a") as f:
        for ip in ips:
            f.write(f"{ip}\n")
    print(f"[🛡️ SUCCESS] IPs saved to {BLOCK_LIST_FILE}")

if __name__ == "__main__":
    analyze_logs()