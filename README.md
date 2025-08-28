🔍 RedRecon - Modular Pentesting Toolkit

RedRecon (RECON_SCANNER) is a simple, beginner-friendly, modular reconnaissance and scanning tool for ethical hackers and cybersecurity students.
It automates basic enumeration tasks and is designed with extensibility in mind using a plugin-based architecture.

✨ Features

🧩 Plugin-based design — easy to extend

🌐 DNS record enumeration

📛 Subdomain enumeration

📂 Directory brute-forcing

🔌 Port scanning (via Nmap)

⚙️ Configurable via JSON

🔇 Quiet / Debug modes

💾 Save output (JSON + summary)

📦 Requirements

Install Python dependencies with:

pip install -r requirements.txt


Also ensure Nmap is installed on your system (system-level dependency).

🔌 Available Plugins

All plugins are located in the /plugins folder:

port_scan → Nmap-based port scanning

dns_enum → DNS record enumeration

subdomain_enum → Find subdomains via crt.sh

dir_bruteforce → Directory brute-forcing on web targets

⚙️ Usage
Run all plugins at once
python main.py -t scanme.nmap.org --all

Run only selected plugins
python main.py -t scanme.nmap.org --plugins port_scan dns_enum

Use a config file
python main.py --config config.json

Save results
python main.py -t scanme.nmap.org --all --output report.json

📑 Options
Option	Description
--target	Target domain (e.g., example.com)
--plugins	List of plugins to run (e.g., port_scan dns_enum)
--all	Run all available plugins
--output	Save results to JSON file
--config	Load scan configuration from JSON file
--verbose	Show detailed output
--quiet	Suppress normal output
--debug	Show debugging information

🛡️ Disclaimer

This tool is for educational purposes and authorized security testing only.
Do not scan systems without permission — unauthorized use is illegal.nmap.org --plugins port_scan dns_enum

Save results:
python main.py -t scanme.nmap.org --all --output report.json
