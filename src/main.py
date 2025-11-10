import concurrent
from ftplib import print_line

import typer
import sys
import socket
from rich.console import Console
from rich.table import Table
from tqdm import tqdm
import ipaddress
from concurrent.futures import ThreadPoolExecutor

app = typer.Typer()
global open_ports
global port_services
global console

open_ports = []
port_services = []
console = Console()

def check_ip(ip : str):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        typer.echo(f"Error: '{ip}' is not a valid IP address")
        sys.exit(1)

def scan_port(ip : str, port : int, timeout = 1):
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

    try:
        s.settimeout(timeout)
        result = s.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
            port_services.append(socket.getservbyport(port))

    except socket.timeout:
        return
    finally:
        s.close()

@app.command(name= "scan")
def cli_main(ip_address = typer.Argument(..., help="IP address to scan"),
         start_port= typer.Option(1, "--start", "-s", help="Lower bound of port to scan"),
         end_port= typer.Option(1024, "--end", "--e", help="Upper bound of ports to scan"),
         concurrency = typer.Option(100, "--concurrency", "-c", help="Number of concurrent threads to use"),
         timeout = typer.Option(1, "--timeout", "-t", help="Timeout for each connection attempt"),
         progress_bar = typer.Option(True, "--progress", "-pb", help="Show progress bar (True/False")
         ):
    if type(ip_address) != str:
        ip_address = str(ip_address)
    if type(start_port) != int:
        start_port = int(start_port)
    if type(end_port) != int:
        end_port = int(end_port)
    if type(concurrency) != int:
        concurrency = int(concurrency)
    if isinstance(timeout, float) != True:
        timeout = int(timeout)


    check_ip(ip_address)
    scan_main(ip_address, start_port, end_port, concurrency, timeout, progress_bar)

def format_output(open_ports : list, port_services : list):
    table = Table(title="Open Ports")
    table.add_column("Port", justify="right", style="cyan", no_wrap=True)
    table.add_column("Service", style="magenta")
    for port in range(len(open_ports)):
        table.add_row(str(open_ports[port]), port_services[port])
    console.print(table)

def scan_main(ip_address : str, start_port : int, end_port : int, concurrency : int = 100, timeout = 1, progress_bar = True):
    """Scan a port on the given IP address."""
    check_ip(ip_address)
    if start_port < end_port:
            # start the threaded scan
        with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
            console.print(f"Starting scan of {ip_address} ports {start_port}-{end_port} \n")
            console.rule("Scan Progress")

            futures = [
                executor.submit(scan_port, ip_address, port, timeout=timeout)
                for port in range(start_port, end_port + 1)
            ]

            for port in tqdm(concurrent.futures.as_completed(futures), total=len(futures), colour="#F25278", disable=not progress_bar):
                pass

        console.print(f"Scan complete.  {len(open_ports)} open port(s) found.")
        format_output(open_ports, port_services)
    else:
        typer.echo("Error: Start port must be less than end port")

if __name__ == '__main__':
    app()
