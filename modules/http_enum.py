import requests

def http_enumeration(domain):
    url = f"http://{domain}"
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
        print(f"[+] HTTP Headers for {url}:")
        for k, v in headers.items():
            print(f"  {k}: {v}")
        
        # Try fetching robots.txt
        robots = requests.get(f"{url}/robots.txt", timeout=5)
        if robots.status_code == 200:
            print("[+] robots.txt found:")
            print(robots.text)
        else:
            print("[-] robots.txt not found")
        
        # Try fetching sitemap.xml
        sitemap = requests.get(f"{url}/sitemap.xml", timeout=5)
        if sitemap.status_code == 200:
            print("[+] sitemap.xml found:")
            print(sitemap.text)
        else:
            print("[-] sitemap.xml not found")
    except Exception as e:
        print(f"[-] HTTP Enumeration failed: {e}")
