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

## Installation (example)

Clone the repo and run with Python:

```bash
   git clone https://github.com/Inval1dUser/spscan.git
   cd spscan
```

create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate
```
or if you are on windows
```bash
source venv/scripts/activate
```

Install
```bash
#install in editable mode
pip install -e .
```
or alternatively

```bash
pip install .
```

## Usage (example)

Scan a single host for ports 20-1024:

```bash
   spscan 127.0.0.1 --start 20 --end 1024
```

Quick scan with a long timeout:

```bash
   spscan 10.0.0.5 --timeout 3
```

## Example output

```
Scanning 192.0.2.10 ports 1-1024
threads: 100
Open: 22
Open: 80
Scan complete. 2 open ports found.
```

## Contributing

1. Fork the repo.
2. Create a feature branch.
3. Open a clear PR with motivation and test(s).
4. Keep changes focused and documented.