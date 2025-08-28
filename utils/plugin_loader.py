import os
import importlib.util

def load_plugins(plugin_dir="plugins"):
    plugins = {}

    for filename in os.listdir(plugin_dir):
        if filename.endswith(".py") and not filename.startswith("__"):
            path = os.path.join(plugin_dir, filename)
            module_name = filename[:-3]  # e.g. "port_scan_plugin"

            spec = importlib.util.spec_from_file_location(module_name, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Use filename (without "_plugin") as plugin key
            plugin_key = module_name.replace("_plugin", "")

            if hasattr(module, "run"):
                plugins[plugin_key] = module
            else:
                print(f"[!] Skipping invalid plugin: {filename}")

    return plugins
