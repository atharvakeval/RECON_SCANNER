# plugins/dir_bruteforce_plugin.py

from modules import dir_bruteforce

# Plugin identifier
name = "dir_bruteforce"

# Metadata for introspection or future plugin manager
metadata = {
    "name": "Directory Bruteforce Plugin",
    "description": "Bruteforces directories on a web server using a wordlist.",
    "author": "YourName",
    "version": "1.0"
}


def run(target, config=None, verbose=False):
    """
    Runs the directory brute force scan.

    Args:
        target (str): The domain or IP to scan.
        config (dict): Optional configuration dictionary.
        verbose (bool): Whether to print verbose output.

    Returns:
        list: A list of discovered directories.
    """
    # Default wordlist path
    wordlist_path = "wordlists/wordlist.txt"

    # Allow config override
    if config and "wordlist" in config:
        wordlist_path = config["wordlist"]

    if verbose:
        print(f"[PLUGIN: dir_bruteforce] Starting directory brute force on {target}")
        print(f"[PLUGIN: dir_bruteforce] Using wordlist: {wordlist_path}")

    # Call the underlying module function
    try:
        results = dir_bruteforce.dir_bruteforce(target, wordlist_path, verbose=verbose)
        return results
    except Exception as e:
        if verbose:
            print(f"[PLUGIN: dir_bruteforce] Error: {e}")
        return []
