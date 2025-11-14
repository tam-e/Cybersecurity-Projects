# log_parser.py
import re
import os

# 1. Define the Regex Pattern
# This pattern is designed to capture the IP address and the HTTP status code (e.g., 401)
LOG_PATTERN = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?"POST /login HTTP/1.1" (\d{3})')

def analyze_logs(log_file_path, threshold=3):
    """
    Analyzes the log file to find repeated login failures.
    """
    # Dictionary to store failed login counts: {'ip_address': count}
    failed_logins = {}
    
    # 2. Check if the log file exists
    if not os.path.exists(log_file_path):
        print(f"[-] Error: Log file not found at {log_file_path}")
        return

    print(f"[*] Analyzing log file: {log_file_path}")
    
    # 3. Read the log file line by line
    with open(log_file_path, 'r') as f:
        for line in f:
            # 4. Use Regex to search for the pattern in each line
            match = LOG_PATTERN.search(line)
            
            if match:
                ip_address = match.group(1)
                status_code = match.group(2)
                
                # 5. Check for a failed login status code (401 is Unauthorized)
                if status_code == '401':
                    # Add to the dictionary or increment the count
                    failed_logins[ip_address] = failed_logins.get(ip_address, 0) + 1

    # 6. Report the potential attacks
    print("\n--- FORENSIC REPORT: Potential Brute-Force Attempts ---")
    
    suspicious_ips = 0
    for ip, count in failed_logins.items():
        if count >= threshold:
            print(f"🚨 ALERT: IP {ip} failed to log in {count} times (Threshold: {threshold})")
            suspicious_ips += 1
        else:
            print(f"[*] IP {ip} failed {count} times (Below threshold)")

    if suspicious_ips == 0:
        print("✅ No suspicious IP addresses found above the failure threshold.")


# --- MAIN PROGRAM EXECUTION ---

if __name__ == "__main__":
    # The log file is in the same folder as this Python script
    LOG_FILE = 'log-analyzer/access.log' 
    
    # In a real-world scenario, you would increase the threshold (e.g., 50 or 100)
    analyze_logs(LOG_FILE, threshold=2)