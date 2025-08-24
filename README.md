# 🔍 RedRecon - Modular Pentesting Toolkit

**RECON_SCANNER** is a simple, beginner-friendly, modular reconnaissance and scanning tool for ethical hackers and cybersecurity students. It is designed to automate basic enumeration tasks and is built with extensibility in mind using a **plugin-based architecture**.

---

## ✨ Features

- 🧩 Plugin-based design — easy to extend
- 🌐 DNS record enumeration
- 📛 Subdomain enumeration
- 📂 Directory brute-forcing
- 🔌 Port scanning (via Nmap)
- ⚙️ Configurable via JSON
- 🔇 Quiet and debug modes
- 💾 Output saved in JSON and summary formats

---

## 📦 Requirements
dnspython
requests
nmap (system-level dependency)
python-nmap (Python wrapper for Nmap)

---

Options
Option	Description
--target	Target domain (e.g. example.com)
--plugins	List of plugins to run (e.g. port_scan dns_enum)
--output	Save results to JSON file
--config	Load scan configuration from a JSON file
--verbose	Show more detailed output
--quiet	Suppress all non-error output
--debug	Show debugging information

🔌 Available Plugins
These plugins are located in the /plugins folder:
port_scan — basic Nmap port scanning
dns_enum — get DNS records
subdomain_enum — find subdomains using a wordlist
dir_bruteforce — directory enumeration on web targets


🛡️ Disclaimer
This tool is for educational purposes and authorized testing only.
Do not scan systems without permission — unauthorized use is illegal.


---
Install dependencies with:

```bash
pip install -r requirements.txt

