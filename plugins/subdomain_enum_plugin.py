# plugins/subdomain_enum_plugin.py

from modules import subdomain_enum

name = "subdomain_enum"

metadata = {
    "name": "Subdomain Enumeration Plugin",
    "description": "Finds subdomains for the target domain.",
    "author": "YourName",
    "version": "1.0"
}

def run(target, config=None, verbose=False):
    """
    Runs subdomain enumeration on the target domain.

    Args:
        target (str): The domain to enumerate subdomains for.
        config (dict, optional): Plugin configuration (unused).
        verbose (bool): Enable verbose output.

    Returns:
        dict: Found subdomains or empty dict on failure.
    """
    if verbose:
        print(f"[PLUGIN: subdomain_enum] Enumerating subdomains for {target}...")

    try:
        results = subdomain_enum.fetch_subdomains(target)
        return results
    except Exception as e:
        if verbose:
            print(f"[PLUGIN: subdomain_enum] Subdomain enumeration failed: {e}")
        return {}
