import concurrent
import typer
import sys
import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor

app = typer.Typer()

def check_ip(ip : str):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        print(f"Error: '{ip}' is not a valid IP address")
        sys.exit(1)

def scan_port(ip : str, port : int):
    """Scan a single port on the given IP address."""
    #print(f"Scanning port {port} on {ip}")
    try:
        target = socket.gethostbyname(ip)
    except socket.gaierror:
        print(f"Error: Hostname '{ip}' could not be resolved")
        return

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))
    if result == 0:
        print("Port {} is open".format(port))
        s.close()
    else:
        s.close()

@app.command(name= "scan")
def cli_main(ip_address = typer.Argument(..., help="IP address to scan"),
         start_port= typer.Option(1, "--start", "-s", help="Lower bound of port to scan"),
         end_port= typer.Option(1024, "--end", "--e", help="Upper bound of ports to scan"),
         concurrency = typer.Option(100, "--concurrency", "-c", help="Number of concurrent threads to use")
         ):
    if type(ip_address) != str:
        ip_address = str(ip_address)
    if type(start_port) != int:
        start_port = int(start_port)
    if type(end_port) != int:
        end_port = int(end_port)
    if type(concurrency) != int:
        concurrency = int(concurrency)

    scan_main(ip_address, start_port, end_port, concurrency)

def scan_main(ip_address : str, start_port : int, end_port : int, concurrency : int = 100):
    """Scan a port on the given IP address."""
    check_ip(ip_address)
    if start_port < end_port:
        if(concurrency < (end_port - start_port)):
            concurrency = (end_port - start_port)
            # start the threaded scan
        with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
            for port in range(start_port, end_port + 1):
                executor.submit(scan_port, ip_address, port)
        print(f"Finished scanning {ip_address}")
    else:
        print("Error: Start port must be less than end port")

if __name__ == '__main__':
    app()
