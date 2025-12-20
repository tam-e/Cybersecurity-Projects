# vt_checker.py
import requests
import json
import sys

# --- CONFIGURATION (REPLACE WITH YOUR KEY) ---
# NOTE: In a real-world tool, you would load this from an environment variable!
API_KEY = "c7441aec4082ed62789eb2d790f2b4e7fce8ee5960b710b37ebabe742319db5a"
VT_URL = "https://www.virustotal.com/api/v3/ip_addresses/"
# ---------------------------------------------

def query_virustotal(indicator):
    """
    Queries the VirusTotal API for information about an IP address.
    """
    if API_KEY == "YOUR_VIRUSTOTAL_API_KEY":
        print("[-] ERROR: Please replace 'YOUR_VIRUSTOTAL_API_KEY' in the script with your actual key.")
        sys.exit()

    # The headers must include the API key for authentication
    headers = {
        "x-apikey": API_KEY,
        "Accept": "application/json"
    }
    
    # Construct the final API endpoint URL
    full_url = VT_URL + indicator
    
    print(f"[*] Querying VirusTotal for: {indicator}...")

    try:
        # Make the GET request
        response = requests.get(full_url, headers=headers)
        
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
        
        # Parse the JSON response into a Python dictionary
        data = response.json()
        
        return data

    except requests.exceptions.HTTPError as errh:
        # Handle specific HTTP errors (e.g., 404 Not Found, 401 Unauthorized)
        print(f"[-] HTTP Error occurred: {errh}")
    except requests.exceptions.RequestException as e:
        # Handle network issues (e.g., connection lost, timeout)
        print(f"[-] Network Error: Could not connect to VirusTotal. {e}")
    except Exception as e:
        print(f"[-] An unexpected error occurred: {e}")
        
    return None

def analyze_and_display(data, indicator):
    """
    Parses the JSON response to extract key security metrics.
    """
    if not data or 'data' not in data:
        print("[-] Could not retrieve valid data.")
        return
        
    # JSON Parsing: Navigating the dictionary structure
    attributes = data['data']['attributes']
    
    # Extract security verdict counts
    malicious_count = attributes['last_analysis_stats'].get('malicious', 0)
    suspicious_count = attributes['last_analysis_stats'].get('suspicious', 0)
    undetected_count = attributes['last_analysis_stats'].get('undetected', 0)
    
    # Extract country and ownership information
    country = attributes.get('country', 'N/A')
    owner = attributes.get('as_owner', 'N/A')

    print("\n--- VIRUSTOTAL REPORT ---")
    print(f"IP Address: {indicator}")
    print(f"Country: {country}")
    print(f"AS Owner (ISP): {owner}")
    print(f"Total Sources Checked: {malicious_count + suspicious_count + undetected_count}")
    print(f"\n[SUMMARY]")
    print(f"🚨 Malicious Detections: {malicious_count}")
    print(f"⚠️ Suspicious Detections: {suspicious_count}")
    
    if malicious_count > 0:
        print("\nALERT: This indicator is confirmed malicious by multiple sources!")


# --- MAIN PROGRAM EXECUTION ---

if __name__ == "__main__":
    print("\n--- VirusTotal IP Query Tool ---")
    
    # Example safe IP (Google DNS) for testing a clean result
    test_ip = "8.8.8.8" 
    
    user_indicator = input(f"Enter IP Address (e.g., {test_ip}): ")
    
    if not user_indicator.strip():
        user_indicator = test_ip
        
    response_data = query_virustotal(user_indicator)
    
    if response_data:
        analyze_and_display(response_data, user_indicator)