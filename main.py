import argparse
import sys
import os
import re
import json
import traceback

# Ensure local packages are discoverable
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.output_writer import save_to_file
from utils.plugin_loader import load_plugins   # ✅ Import plugin loader


def is_valid_domain(domain):
    pattern = r'^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
    return re.match(pattern, domain) is not None


def print_debug(debug, message):
    if debug:
        print("[DEBUG]", message)


def print_info(quiet, message):
    if not quiet:
        print(message)


def generate_summary(results, target, quiet):
    if quiet:
        return

    summary = []
    summary.append("\n" + "=" * 40)
    summary.append("         RedRecon Summary")
    summary.append("=" * 40)
    summary.append(f"[+] Target: {target}")

    if 'port_scan' in results and results['port_scan']:
        open_ports = len(results['port_scan'].get('open_ports', []))
        summary.append(f"[+] Open Ports: {open_ports}")

    if 'dns_enum' in results and results['dns_enum']:
        summary.append(f"[+] DNS Records Found: {len(results['dns_enum'])}")

    if 'subdomain_enum' in results and results['subdomain_enum']:
        summary.append(f"[+] Subdomains Found: {len(results['subdomain_enum'])}")

    if 'dir_bruteforce' in results and results['dir_bruteforce']:
        summary.append(f"[+] Directories Found: {len(results['dir_bruteforce'])}")

    summary.append("=" * 40)
    print("\n".join(summary))


def generate_summary_text(results, target):
    summary = []
    summary.append("RedRecon Summary")
    summary.append(f"Target: {target}")

    if 'port_scan' in results and results['port_scan']:
        open_ports = len(results['port_scan'].get('open_ports', []))
        summary.append(f"Open Ports: {open_ports}")

    if 'dns_enum' in results and results['dns_enum']:
        summary.append(f"DNS Records: {len(results['dns_enum'])}")

    if 'subdomain_enum' in results and results['subdomain_enum']:
        summary.append(f"Subdomains Found: {len(results['subdomain_enum'])}")

    if 'dir_bruteforce' in results and results['dir_bruteforce']:
        summary.append(f"Directories Found: {len(results['dir_bruteforce'])}")

    return "\n".join(summary)


def main():
    # --- Stage 1: parse only --config ---
    pre_parser = argparse.ArgumentParser(add_help=False)
    pre_parser.add_argument('--config', help='Load options from config JSON file')
    pre_args, remaining_argv = pre_parser.parse_known_args()

    defaults = {}

    if pre_args.config:
        try:
            with open(pre_args.config, 'r') as f:
                config_data = json.load(f)
                defaults.update(config_data)
                print(f"[+] Loaded config from {pre_args.config}")
        except Exception as e:
            print(f"[-] Failed to read config: {e}")
            sys.exit(1)

    # --- Stage 2: full parser, with defaults from config ---
    parser = argparse.ArgumentParser(description="RedRecon - Plugin-based Pentest Tool")

    parser.add_argument('--target', '-t',
                        required='target' not in defaults,
                        help='Target domain (e.g., example.com)')
    parser.add_argument('--plugins', nargs='+', help='List of plugins to run (e.g., port_scan dns_enum)')
    parser.add_argument('--all', action='store_true', help='Run all available plugins')
    parser.add_argument('--output', '-o', help='Save output to JSON file')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    parser.add_argument('--quiet', action='store_true', help='Suppress normal output')
    parser.add_argument('--debug', action='store_true', help='Show debug messages')
    parser.add_argument('--config', help='Load options from config JSON file')  # keep for clarity

    parser.set_defaults(**defaults)

    args = parser.parse_args(remaining_argv)

    if args.quiet and args.debug:
        print("[-] You can't use --quiet and --debug together.")
        sys.exit(1)

    if not is_valid_domain(args.target):
        print("[-] Invalid domain name.")
        sys.exit(1)

    all_plugins = load_plugins()
    results = {}

    if args.all:
        args.plugins = list(all_plugins.keys())

    if not args.plugins:
        print("[!] No plugins specified. Use --plugins or --all.")
        print(f"[+] Available plugins: {', '.join(all_plugins.keys())}")
        sys.exit(1)

    for plugin_name in args.plugins:
        plugin = all_plugins.get(plugin_name)
        if not plugin:
            print(f"[!] Plugin '{plugin_name}' not found.")
            continue

        if not args.quiet:
            print(f"[+] Running plugin: {plugin_name}")

        try:
            result = plugin.run(args.target, config=None, verbose=args.verbose)

            if result is None:
                results[plugin_name] = {}
            else:
                results[plugin_name] = result

        except Exception as e:
            print(f"[!] Plugin '{plugin_name}' failed: {e}")
            if args.debug:
                traceback.print_exc()
            results[plugin_name] = {}

    if args.output:
        save_to_file(results, args.output)
        if not args.quiet:
            print(f"[+] Results saved to {args.output}")

    generate_summary(results, args.target, args.quiet)


if __name__ == "__main__":
    main()
