# plugins/dns_enum_plugin.py

from modules import dns_enum

name = "dns_enum"

metadata = {
    "name": "DNS Enumeration Plugin",
    "description": "Fetches DNS records (A, MX, NS, etc.) for a given domain.",
    "author": "YourName",
    "version": "1.0"
}


def run(target, config=None, verbose=False):
    """
    Runs DNS enumeration on the target domain.

    Args:
        target (str): Domain to enumerate.
        config (dict, optional): Plugin config (unused here).
        verbose (bool): Enable verbose output.

    Returns:
        dict: DNS records or empty dict on failure.
    """
    if verbose:
        print(f"[PLUGIN: dns_enum] Fetching DNS records for {target}...")

    try:
        results = dns_enum.fetch_dns_records(target)
        return results
    except Exception as e:
        if verbose:
            print(f"[PLUGIN: dns_enum] Error during DNS enumeration: {e}")
        return {}
