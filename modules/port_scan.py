import nmap

def run_nmap_scan(target):
    print(f"[+] Running Nmap scan on {target}...")
    nm = nmap.PortScanner()

    try:
        nm.scan(hosts=target, arguments='-sS -T4 -Pn')
        for host in nm.all_hosts():
            print(f"\n[+] Host: {host} ({nm[host].hostname()})")
            print(f"    State: {nm[host].state()}")
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                for port in sorted(lport):
                    state = nm[host][proto][port]['state']
                    name = nm[host][proto][port]['name']
                    print(f"    Port: {port}\tState: {state}\tService: {name}")
    except Exception as e:
        print(f"[-] Error running Nmap: {e}")
