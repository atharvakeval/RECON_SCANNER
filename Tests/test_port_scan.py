from modules import port_scan

def test_run_nmap_scan():
    result = port_scan.run_nmap_scan("scanme.nmap.org")
    assert isinstance(result, dict)
    assert "open_ports" in result
