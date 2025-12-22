import requests

# The 5 "Digital Deadbolts" we are checking for
SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Content-Security-Policy",
    "Permissions-Policy"
]

def scan_website(url):
    # Ensure the URL starts with http
    if not url.startswith("http"):
        url = "https://" + url

    print(f"\n--- 🔍 SCANNING: {url} ---")
    
    try:
        # We send a "HEAD" request to just get the headers without downloading the whole page
        response = requests.head(url, timeout=5, allow_redirects=True)
        headers = response.headers
        
        missing_headers = []

        for header in SECURITY_HEADERS:
            if header in headers:
                print(f"[✅] {header}: FOUND")
            else:
                print(f"[❌] {header}: MISSING")
                missing_headers.append(header)

        # Summary of Findings
        if missing_headers:
            print(f"\n[⚠️  RESULT] Vulnerabilities Detected! {len(missing_headers)} security headers are missing.")
        else:
            print("\n[🛡️  RESULT] Excellent! All critical security headers are present.")

    except Exception as e:
        print(f"[!] Error connecting to {url}: {e}")

if __name__ == "__main__":
    target = input("Enter a website URL to scan (e.g., google.com): ")
    scan_website(target)