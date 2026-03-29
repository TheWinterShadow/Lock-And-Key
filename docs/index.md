# Lock-And-Key

[![CI Tests](https://github.com/TheWinterShadow/lock-and-key/actions/workflows/ci.yml/badge.svg)](https://github.com/TheWinterShadow/lock-and-key/actions/workflows/ci.yml)
[![Build & Package](https://github.com/TheWinterShadow/lock-and-key/actions/workflows/python-package.yml/badge.svg)](https://github.com/TheWinterShadow/lock-and-key/actions/workflows/python-package.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/lock-and-key.svg)](https://pypi.org/project/lock-and-key)

**Lock & Key** is a comprehensive cloud security scanner that analyzes access policies and resource-based policies across multiple cloud providers to identify security vulnerabilities, excessive permissions, and compliance issues.

## Features

- ☁️ **Multi-Cloud Support**: AWS (fully implemented), Azure (in progress), GCP (in progress)
- 🔍 **Comprehensive Policy Analysis**: Scans IAM policies and resource-based policies across all supported services
- 🛡️ **Security Vulnerability Detection**: Identifies privilege escalation risks, wildcard permissions, and administrative access
- 💻 **Interactive CLI**: User-friendly command-line interface with rich formatting and progress indicators
- 📊 **Detailed Reporting**: Generates JSON reports with actionable findings and recommendations
- ⚖️ **Least Privilege Analysis**: Highlights violations of the principle of least privilege

## Quick Start

### Installation

```console
# Basic installation
pip install lock-and-key

# With enhanced AWS support (better IDE experience)
pip install lock-and-key[aws]

# For developers (includes testing and linting tools)
pip install lock-and-key[dev]

# Everything included
pip install lock-and-key[all]
```

### Run Your First Scan

```console
# Interactive mode (recommended for first-time users)
lock-and-key interactive

# Direct AWS scan with profile
lock-and-key scan --provider AWS --profile my-profile
```

### Options

- `--output-dir`: Specify output directory for reports (default: `./reports`)
- `--provider`: Choose cloud provider (AWS, Azure, GCP)
- Various credential options for each provider
