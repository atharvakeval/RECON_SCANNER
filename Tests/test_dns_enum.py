import unittest
from modules import dns_enum

class TestDNSEnum(unittest.TestCase):
    def test_fetch_dns_records_valid(self):
        domain = "example.com"
        records = dns_enum.fetch_dns_records(domain)
        self.assertIsInstance(records, dict)
        self.assertIn('A', records)

    def test_fetch_dns_records_invalid(self):
        domain = "invalid_domain"
        records = dns_enum.fetch_dns_records(domain)
        self.assertEqual(records, {})  # Expect empty dict on failure

if __name__ == "__main__":
    unittest.main()
