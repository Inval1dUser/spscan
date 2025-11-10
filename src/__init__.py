import socket
import socket
import typer
import sys


def grab_banner(ip : str, port : int, timeout = 1):
    banner = None
    s = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((ip, port))
        # receive banner
        banner = s.recv(1024).decode().strip()
    except socket.timeout:
        # No banner received within timeout
        pass
    except socket.error as e:
        typer.echo(f"Error: {e}")
    except UnicodeDecodeError:
        # Handle non-text banners
        typer.echo("Warning: Received non-text banner")
    finally:
        if s:
            s.close()
        return banner

if __name__ == '__main__':
    for port in range(1, 1024):
        banner = grab_banner("8.8.8.8", port, timeout=0.1)
        if banner:
            print(f"Port {port}: {banner}")