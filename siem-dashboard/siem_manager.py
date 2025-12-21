import os

# --- PATHS TO YOUR OTHER PROJECTS ---
# We are reaching out to the logs created by your other scripts
NOC_LOG = "noc-monitor/network_stats.log"
SECURITY_LOG = "security-automation/blocked_ips.txt"

def get_noc_summary():
    if not os.path.exists(NOC_LOG):
        return "No Data"
    
    with open(NOC_LOG, "r") as f:
        lines = f.readlines()
        total_checks = len(lines)
        outages = sum(1 for line in lines if "OFFLINE" in line)
        return f"{total_checks} Checks | {outages} Outages Detected"

def get_security_summary():
    if not os.path.exists(SECURITY_LOG):
        return "0 IPs Blocked"
    
    with open(SECURITY_LOG, "r") as f:
        blocked_ips = len(f.readlines())
        return f"{blocked_ips} Malicious IPs Blacklisted"

def run_siem():
    print("="*50)
    print("🛡️  MASTER SIEM DASHBOARD - CENTRAL COMMAND")
    print("="*50)
    
    # Section 1: Network Health (From Project 8)
    print(f"\n[🌐 NETWORK OPS CENTER]")
    print(f"Status: {get_noc_summary()}")
    
    # Section 2: Security Automation (From Project 9)
    print(f"\n[🔒 SECURITY OPERATIONS]")
    print(f"Status: {get_security_summary()}")
    
    print("\n" + "="*50)
    print("SIEM Summary: System is currently MONITORING & PROTECTING.")
    print("="*50)

if __name__ == "__main__":
    run_siem()