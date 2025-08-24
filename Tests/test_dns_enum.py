from modules import dns_enum

def test_fetch_dns_records():
    result = dns_enum.fetch_dns_records("example.com")
    assert isinstance(result, dict)
    assert "A" in result
