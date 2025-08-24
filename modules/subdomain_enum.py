import requests
import time

def fetch_subdomains(domain, retries=3, backoff=5):
    print(f"[+] Fetching subdomains for {domain} via crt.sh...\n")

    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    attempt = 0

    while attempt < retries:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                print(f"[-] Error querying crt.sh: HTTP {response.status_code}")
                return []

            json_data = response.json()
            subdomains = set()

            for entry in json_data:
                name = entry['name_value']
                # crt.sh returns domains sometimes with multiple names separated by \n
                for sub in name.split('\n'):
                    if sub.endswith(domain):
                        subdomains.add(sub.lower())
            
            print(f"[+] Found {len(subdomains)} unique subdomains:\n")
            for sub in sorted(subdomains):
                print(f"  {sub}")
            
            return sorted(subdomains)

        except requests.exceptions.Timeout:
            attempt += 1
            print(f"[-] Timeout fetching subdomains from crt.sh. Retrying {attempt}/{retries} after {backoff}s...")
            time.sleep(backoff)

        except requests.exceptions.RequestException as e:
            print(f"[-] Request error fetching subdomains: {e}")
            break

        except Exception as e:
            print(f"[-] Unexpected error fetching subdomains: {e}")
            break

    print("[-] Failed to fetch subdomains after retries.")
    return []
