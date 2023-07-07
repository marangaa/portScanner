import socket
from typing import Dict
import ipaddress


class PortScanner:
    def scan(self, ip: str, udp: bool, from_port: int, to_port: int) -> Dict[int, bool]:
        # Check if the IP address is valid
        try:
            ipaddress.IPv4Address(ip)
        except ipaddress.AddressValueError:
            return {}

        # Check if the port range is valid
        if from_port < 0 or to_port < 0:
            return {}

        # Initialize the result dictionary
        results = {}

        # Perform the scanning
        for port in range(from_port, to_port + 1):
            try:
                # Create a socket object
                if udp:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                else:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                # Set a timeout for the receive operation (only for UDP)
                if udp:
                    sock.settimeout(1.0)

                if udp:
                    # Send a test message to the port
                    sock.sendto(b"Test", (ip, port))

                    # Receive data from the port
                    data, _ = sock.recvfrom(1024)

                    # If data is received, the port is open
                    results[port] = True
                else:
                    # Attempt to connect to the port
                    sock.connect((ip, port))

                    # If the connection is successful, the port is open
                    results[port] = True

                # Close the socket
                sock.close()
            except Exception:
                # If any exception occurs, consider the port closed
                results[port] = False

        return results
