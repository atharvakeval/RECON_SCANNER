import ssl
import socket
import datetime

def get_ssl_info(domain):
    context = ssl.create_default_context()
    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            cert = ssock.getpeercert()
            print(f"Certificate for {domain}:")
            print(f"  Subject: {cert['subject']}")
            print(f"  Issuer: {cert['issuer']}")
            print(f"  Valid from: {cert['notBefore']}")
            print(f"  Valid until: {cert['notAfter']}")
