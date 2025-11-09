import concurrent
import typer
import sys
import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor

app = typer.Typer()
global open_ports
open_ports = []

def check_ip(ip : str):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        typer.echo(f"Error: '{ip}' is not a valid IP address")
        sys.exit(1)

def scan_port(ip : str, port : int, timeout : int = 1):
    """Scan a single port on the given IP address."""
    #typer.echo(f"Scanning port {port} on {ip}")
    try:
        target = socket.gethostbyname(ip)
    except socket.gaierror:
        typer.echo(f"Error: Hostname '{ip}' could not be resolved")
        return

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        typer.echo(f"Error: Failed to create socket")
        return

    banner = None

    try:
        s.settimeout(timeout)
        result = s.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
            try:
                banner_bytes = s.recv(1024)
                if banner_bytes:
                    banner = banner_bytes.decode(errors="ignore").strip()
            except:
                pass
            typer.echo(f"Open: {port}/{banner}")
    except socket.timeout:
        return
    finally:
        s.close()

@app.command(name= "scan")
def cli_main(ip_address = typer.Argument(..., help="IP address to scan"),
         start_port= typer.Option(1, "--start", "-s", help="Lower bound of port to scan"),
         end_port= typer.Option(1024, "--end", "--e", help="Upper bound of ports to scan"),
         concurrency = typer.Option(100, "--concurrency", "-c", help="Number of concurrent threads to use"),
         timeout = typer.Option(1, "--timeout", "-t", help="Timeout for each connection attempt")
         ):
    if type(ip_address) != str:
        ip_address = str(ip_address)
    if type(start_port) != int:
        start_port = int(start_port)
    if type(end_port) != int:
        end_port = int(end_port)
    if type(concurrency) != int:
        concurrency = int(concurrency)
    if type(timeout) != int:
        timeout = int(timeout)

    check_ip(ip_address)
    scan_main(ip_address, start_port, end_port, concurrency, timeout)

def scan_main(ip_address : str, start_port : int, end_port : int, concurrency : int = 100, timeout : int = 1):
    """Scan a port on the given IP address."""
    check_ip(ip_address)




    if start_port < end_port:
            # start the threaded scan
        with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
            typer.echo(f"Scanning {ip_address} ports {start_port}-{end_port} \n"
                       f"threads: {concurrency}")
            for port in range(start_port, end_port + 1):
                executor.submit(scan_port, ip_address, port, timeout=timeout)
        typer.echo(f"Scan complete.  {len(open_ports)} open ports found.")
    else:
        typer.echo("Error: Start port must be less than end port")

if __name__ == '__main__':
    scan_main(ip_address="8.8.8.8", start_port=1, end_port=1024, concurrency=1000, timeout=1)