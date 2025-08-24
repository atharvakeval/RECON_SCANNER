import subprocess

def run_nuclei(target):
    try:
        print(f"[+] Running nuclei scan on {target}...")
        result = subprocess.run(["nuclei", "-u", target], capture_output=True, text=True, timeout=300)
        print(result.stdout)
    except Exception as e:
        print(f"[-] Nuclei scan failed: {e}")
