from modules import subdomain_enum

def test_fetch_subdomains():
    subdomains = subdomain_enum.fetch_subdomains("example.com")
    assert isinstance(subdomains, list)
    assert "example.com" in subdomains
