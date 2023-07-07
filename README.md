# PortScanner

The `PortScanner` is a Python class that allows you to scan ports on a given IP address using TCP or UDP protocols. It provides a simple and straightforward way to check the status of multiple ports within a specified range.

## Features

- Scans ports on a given IP address using TCP or UDP protocols.
- Returns a dictionary with port numbers and their status (open/closed).
- Supports both IPv4 and IPv6 addresses.
- Handles invalid IP addresses and port ranges gracefully.

## Requirements

- Python 3.8 or above.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/PortScanner.git

from port_scanner import PortScanner

scanner = PortScanner()

ip_address = "127.0.0.1"
use_udp = True
from_port = 10000
to_port = 10010

results = scanner.scan(ip_address, use_udp, from_port, to_port)

print(results)
# Output: {10000: False, 10001: True, 10002: True, ...}
