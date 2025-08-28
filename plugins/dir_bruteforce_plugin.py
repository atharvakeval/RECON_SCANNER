import requests
import os

name = "dir_bruteforce"

def run(target, config=None, verbose=False, wordlist=None):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
    # now base_dir = D:\cyber security\project\RedRecon

    fallback_wordlists = [
        os.path.join(base_dir, "wordlists", "wordlist.txt"),
        os.path.join(base_dir, "wordlists", "common.txt"),
        os.path.join(base_dir, "wordlists", "directory-list.txt"),
    ]

    # Pick wordlist
    wordlist_path = None
    if wordlist and os.path.isfile(wordlist):
        wordlist_path = wordlist
    else:
        for wl in fallback_wordlists:
            if os.path.isfile(wl):
                wordlist_path = wl
                break

    if not wordlist_path:
        print("[-] No valid wordlist found. Please place one in 'wordlists/' or use --wordlist")
        return {}

    print(f"[+] Using wordlist: {wordlist_path}")

    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            words = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"[-] Failed to load wordlist: {e}")
        return {}

    found_dirs = []
    base_url = f"http://{target}".rstrip("/")

    for word in words:
        url = f"{base_url}/{word}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code in [200, 301, 302, 403]:
                found_dirs.append({"url": url, "status": response.status_code})
                if verbose:
                    print(f"[+] Found: {url} (Status: {response.status_code})")
            elif verbose:
                print(f"[-] Not found: {url}")
        except requests.RequestException:
            if verbose:
                print(f"[!] Error accessing {url}")
            continue

    return {"directories": found_dirs}
