import dns.resolver

def fetch_dns_records(domain):
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME']
    results = {}

    print(f"[+] Fetching DNS records for {domain}...\n")

    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            records = [r.to_text() for r in answers]
            results[record_type] = records
            print(f"{record_type} records:")
            for r in records:
                print(f"  {r}")
            print()
        except Exception as e:
            print(f"  Could not fetch {record_type} records: {e}\n")
    
    return results

