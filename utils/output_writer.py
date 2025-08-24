import os
import json
import csv

def save_to_file(data, filepath):
    if not filepath:
        print("[-] No output file specified, skipping save.")
        return

    os.makedirs(os.path.dirname(filepath) or '.', exist_ok=True)
    ext = os.path.splitext(filepath)[1].lower()

    if ext == '.json':
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"[+] JSON results saved to {filepath}")

    elif ext == '.csv':
        # Simple CSV export: flatten the data depending on structure
        # Example: export port scan results only
        if 'ports' in data:
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Host', 'Port', 'State', 'Service'])
                for host, ports in data['ports'].items():
                    for port_info in ports:
                        writer.writerow([host, port_info['port'], port_info['state'], port_info['service']])
            print(f"[+] CSV results saved to {filepath}")
        else:
            print("[-] CSV export only supports port scan results currently.")

    elif ext == '.md':
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("# Scan Report\n\n")

            if 'ports' in data:
                f.write("## Port Scan Results\n\n")
                for host, ports in data['ports'].items():
                    f.write(f"### {host}\n\n")
                    f.write("| Port | State | Service |\n")
                    f.write("|------|-------|---------|\n")
                    for port_info in ports:
                        f.write(f"| {port_info['port']} | {port_info['state']} | {port_info['service']} |\n")
                    f.write("\n")

            if 'dns' in data:
                f.write("## DNS Records\n\n")
                for record_type, records in data['dns'].items():
                    f.write(f"### {record_type} Records\n")
                    for record in records:
                        f.write(f"- {record}\n")
                    f.write("\n")

            if 'subdomains' in data:
                f.write("## Subdomains\n\n")
                for sub in data['subdomains']:
                    f.write(f"- {sub}\n")
                f.write("\n")

        print(f"[+] Markdown results saved to {filepath}")

    else:
        print(f"[-] Unsupported output format: {ext}. Supported: .json, .csv, .md")
