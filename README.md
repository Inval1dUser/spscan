# Port Scanner

A simple, minimal CLI port scanner written in Python.
This repository provides a lightweight proof-of-concept scanner for learning and local testing. Use only on hosts and networks you own or have explicit permission to scan. ([GitHub][1])

## Features

* Single-host TCP port scanning.
* Range and single-port support (example flags shown).
* Fast configurable timeout and concurrency hints.
* Minimal dependencies. Designed for learning and demonstrations.

## Warning — Legal & Ethical

Port scanning can be considered intrusive. Only scan hosts you own or are explicitly authorized to test. The author and this repository accept no liability for misuse.

## Requirements

* Python 3.8+ (installed on most systems)
* (Optional) `pip` for installing dev/test tools

> The codebase is Python. Confirm exact runtime and dependency versions in `pyproject.toml` or your chosen packaging file. ([GitHub][1])

## Installation (example)

Clone the repo and run with Python:

```bash
git clone https://github.com/Inval1dUser/Port_Scanner.git
cd Port_Scanner
# Optionally create a virtual environment
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate      # Windows PowerShell

# If there is a project packaging file, install dependencies:
# pip install -r requirements.txt
```

## Usage (example)

The exact CLI flags depend on the implementation. Below are safe example usages you can adapt.

Scan a single host for common ports:

```bash
python -m port_scanner --host 192.0.2.10 --ports 20-1024
```

Scan specific ports:

```bash
python -m port_scanner --host example.com --ports 22,80,443
```

Quick scan with a short timeout:

```bash
python -m port_scanner --host 10.0.0.5 --ports 1-1024 --timeout 0.5
```

Show help (replace `port_scanner` with actual module/script name if different):

```bash
python -m port_scanner --help
```

> Replace `python -m port_scanner` with the actual entry point (for example `python src/main.py`) if your repository uses a different layout. Update this section to match the real CLI once confirmed.

## Configuration

List any environment variables or config file format here. Example:

```text
# port_scanner.conf (optional)
host = 192.0.2.10
ports = 1-1024
timeout = 1.0
concurrency = 100
```

## Example output

Provide a sample of what the scanner prints to help users interpret results:

```
Scanning 192.0.2.10 ports 1-1024
Open: 22/tcp   (ssh)
Open: 80/tcp   (http)
Closed: 23/tcp
Scan complete. 2 open ports found.
```

## Development & Tests

* Use a virtual environment.
* Add unit tests for core scanning logic. Avoid network tests that hit external hosts unless running in an isolated test lab.
* Consider fuzzing or property-based tests for parsing and range logic.

## Contributing

1. Fork the repo.
2. Create a feature branch.
3. Open a clear PR with motivation and test(s).
4. Keep changes focused and documented.
   
## License


