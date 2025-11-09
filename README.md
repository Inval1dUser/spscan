# spscan

A simple and efficient port scanner built with Python and Typer. Designed for developers and security enthusiasts who want a quick tool to check open ports on a given host.

## Table of Contents

* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Examples](#examples)
* [Configuration](#configuration)
* [Dependencies](#dependencies)
* [Troubleshooting](#troubleshooting)
* [Contributing](#contributing)
* [License](#license)
* [Author](#author)

## Features

* Scan a single port or a range of ports
* Fast asynchronous execution
* Simple command-line interface using [Typer](https://typer.tiangolo.com/)
* Written in modern Python (3.11+)

## Installation

To install the project, clone the repository and install it using `pip`:

```bash
git clone https://github.com/Inval1dUser/Port_Scanner.git
cd Port_Scanner
pip install .
```

Or install directly from the repository:

```bash
pip install git+https://github.com/Inval1dUser/Port_Scanner.git
```

## Usage

After installation, use the `spscan` CLI:

```bash
spscan [OPTIONS] HOST
```

### Options

* `--start-port`, `-s` — Starting port (default: 1)
* `--end-port`, `-e` — Ending port (default: 1024)
* `--timeout`, `-t` — Timeout in seconds (default: 1)

## Examples

Scan a single port:

```bash
spscan -s 80 -e 80 example.com
```

Scan a range of ports:

```bash
spscan -s 1 -e 100 example.com
```

Set a custom timeout:

```bash
spscan -s 1 -e 100 -t 2 example.com
```

## Configuration

No additional configuration is required. The CLI tool accepts runtime arguments as shown above.

## Dependencies

* [Typer](https://typer.tiangolo.com/): For CLI interface

## Troubleshooting

* **Permission denied**: Ensure you're running the command with appropriate privileges. Some ports (below 1024) may require root access.
* **Slow scan**: Try adjusting the timeout or scanning fewer ports at once.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests on [GitHub](https://github.com/Inval1dUser/Port_Scanner).

## License

This project is licensed under the MIT License.

## Author

**Beck Chandler**
[becktchandler@gmail.com](mailto:becktchandler@gmail.com)

---

Let me know if you'd like to include things like test instructions, CI/CD setup, or add badges (like PyPI, version, or license) at the top.
