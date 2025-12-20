import subprocess
import time
import platform
import os
from datetime import datetime

# --- CONFIGURATION ---
TARGETS = ["8.8.8.8", "1.1.1.1", "google.com", "127.0.0.1"]
INTERVAL = 5 
LOG_FILE = "network_stats.log"
LATENCY_THRESHOLD = 100  # Threshold in milliseconds for Yellow alert

# --- ANSI COLOR CODES ---
# Initialize Windows terminal to support colors if needed
if platform.system().lower() == 'windows':
    os.system('color')

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

def ping_target(target):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', target]
    
    start_time = time.time()
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        end_time = time.time()
        
        if result.returncode == 0:
            latency = round((end_time - start_time) * 1000, 2)
            return "UP", latency
        else:
            return "DOWN", None
    except Exception:
        return "ERROR", None

def run_dashboard():
    print(f"\n{'-'*15} 🖥️ NOC NETWORK DASHBOARD {'-'*15}")
    print(f"Monitoring: {', '.join(TARGETS)}")
    print(f"Alert Threshold: >{LATENCY_THRESHOLD}ms | Press Ctrl+C to stop.\n")
    
    try:
        while True:
            timestamp = datetime.now().strftime("%H:%M:%S")
            for target in TARGETS:
                status, latency = ping_target(target)
                target_fmt = target.ljust(15)
                
                if status == "UP":
                    # --- THRESHOLD LOGIC ---
                    if latency > LATENCY_THRESHOLD:
                        # Highlight yellow if latency is high
                        print(f"[{timestamp}] {YELLOW}[⚠️ HIGH LATENCY]{RESET} {target_fmt} | {latency}ms")
                    else:
                        # Print green if latency is normal
                        print(f"[{timestamp}] {GREEN}[✅ ONLINE]{RESET}       {target_fmt} | {latency}ms")
                else:
                    # Print red if target is offline
                    print(f"[{timestamp}] {RED}[❌ OFFLINE]{RESET}      {target_fmt} | ALERT: UNREACHABLE!")

            print(f"{'-'*50}")
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print(f"\n{YELLOW}[!] Dashboard stopped by user.{RESET}")

if __name__ == "__main__":
    run_dashboard()
# --- ADD THIS TO CONFIGURATION SECTION ---
MAX_LOG_SIZE = 100 * 200  # 100 KB limit

def log_result(target, status, latency):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    latency_str = f"{latency}ms" if latency else "N/A"
    log_entry = f"[{timestamp}] Target: {target} | Status: {status} | Latency: {latency_str}\n"
    
    # --- LOG ROTATION LOGIC ---
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > MAX_LOG_SIZE:
        backup_file = f"network_stats_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log.old"
        os.rename(LOG_FILE, backup_file)
        print(f"{YELLOW}[!] Log size exceeded. Rotating log to {backup_file}{RESET}")
    
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)