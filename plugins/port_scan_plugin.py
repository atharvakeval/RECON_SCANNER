# plugins/port_scan_plugin.py

from modules import port_scan as ps

name = "port_scan"

metadata = {
    "name": "Port Scanning Plugin",
    "description": "Performs an Nmap-based port scan on the target.",
    "author": "YourName",
    "version": "1.0"
}

def run(target, config=None, verbose=False):
    """
    Runs a port scan on the target domain.

    Args:
        target (str): The domain or IP to scan.
        config (dict, optional): Plugin configuration (unused).
        verbose (bool): Enable verbose output.

    Returns:
        dict: Scan results or empty dict on failure.
    """
    if verbose:
        print(f"[PLUGIN: port_scan] Running port scan on {target}...")

    try:
        results = ps.run_nmap_scan(target)
        return results
    except Exception as e:
        if verbose:
            print(f"[PLUGIN: port_scan] Port scan failed: {e}")
        return {}
