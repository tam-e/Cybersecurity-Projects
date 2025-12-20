import os
from datetime import datetime

LOG_FILE = "network_stats.log"

def generate_summary():
    if not os.path.exists(LOG_FILE):
        print(f"[!] Error: {LOG_FILE} not found. Run the dashboard first!")
        return

    stats = {} # Structure: { target: [latency1, latency2, ...] }
    outages = 0
    total_checks = 0

    print(f"--- 📊 DAILY NOC NETWORK SUMMARY ({datetime.now().strftime('%Y-%m-%d')}) ---")

    with open(LOG_FILE, "r") as f:
        for line in f:
            total_checks += 1
            # Simple parsing of the log line
            try:
                parts = line.split("|")
                target = parts[1].split(":")[1].strip()
                status = parts[2].split(":")[1].strip()
                
                if status == "UP":
                    latency_raw = parts[3].split(":")[1].strip().replace("ms", "")
                    latency = float(latency_raw)
                    
                    if target not in stats:
                        stats[target] = []
                    stats[target].append(latency)
                else:
                    outages += 1
            except (IndexError, ValueError):
                continue

    # Display results
    print(f"Total Checks Performed: {total_checks}")
    print(f"Total Connection Failures: {outages}")
    print(f"{'-'*50}")
    print(f"{'Target Address':<20} | {'Avg Latency':<15} | {'Status'}")
    print(f"{'-'*50}")

    for target, latencies in stats.items():
        avg_latency = round(sum(latencies) / len(latencies), 2)
        
        # Determine status based on average
        if avg_latency < 20:
            health = "🟢 EXCELLENT"
        elif avg_latency < 1000:
            health = "🟡 STABLE"
        else:
            health = "🔴 CONGESTED"
            
        print(f"{target:<20} | {avg_latency:<15} | {health}")

if __name__ == "__main__":
    generate_summary()