# Lock-And-Key

[![Documentation](https://github.com/TheWinterShadow/lock-and-key/actions/workflows/docs.yml/badge.svg)](https://github.com/TheWinterShadow/lock-and-key/actions/workflows/docs.yml)
[![CI Tests](https://github.com/TheWinterShadow/lock-and-key/actions/workflows/ci.yml/badge.svg)](https://github.com/TheWinterShadow/lock-and-key/actions/workflows/ci.yml)
[![Build & Package](https://github.com/TheWinterShadow/lock-and-key/actions/workflows/python-package.yml/badge.svg)](https://github.com/TheWinterShadow/lock-and-key/actions/workflows/python-package.yml)

[![PyPI - Version](https://img.shields.io/pypi/v/lock-and-key.svg)](https://pypi.org/project/lock-and-key)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/lock-and-key.svg)](https://pypi.org/project/lock-and-key)
[![Documentation](https://img.shields.io/badge/docs-latest-blue.svg)](https://thewintershadow.github.io/Lock-And-Key/)
[![GitHub](https://img.shields.io/github/license/TheWinterShadow/lock-and-key)](https://github.com/TheWinterShadow/lock-and-key/blob/main/LICENSE.txt)

**Lock & Key** is a comprehensive cloud security scanner that analyzes access policies and resource-based policies across multiple cloud providers to identify security vulnerabilities, excessive permissions, and compliance issues.

📖 **[Full Documentation](https://thewintershadow.github.io/Lock-And-Key/)** | 🚀 **[Quick Start](#quick-start)** | 💻 **[Installation](#installation)**

## Repository Information

- **Name**: lock-and-key
- **Description**: Comprehensive cloud security scanner for IAM and resource-based policies  
- **Homepage**: https://thewintershadow.github.io/Lock-And-Key/
- **Topics**: security, cloud, aws, azure, gcp, iam, scanner, cybersecurity, policies
- **License**: MIT

## Documentation

The complete documentation is available at: https://thewintershadow.github.io/Lock-And-Key/

## Quick Links

- 📖 [Documentation](https://thewintershadow.github.io/Lock-And-Key/)
- 🚀 [Installation Guide](https://thewintershadow.github.io/Lock-And-Key/installation.html)
- 💻 [API Reference](https://thewintershadow.github.io/Lock-And-Key/api.html) 
- 🛠️ [Development Guide](https://thewintershadow.github.io/Lock-And-Key/development.html)
- 🐛 [Report Issues](https://github.com/TheWinterShadow/lock-and-key/issues)
- 📦 [PyPI Package](https://pypi.org/project/lock-and-key/)

## Repository Features

- ✅ Issues enabled
- ✅ GitHub Pages enabled
- ✅ Security scanning enabled
- ✅ Automated documentation deployment
- ✅ Comprehensive test suite
- ✅ CI/CD pipeline

## Features

- **Multi-Cloud Support**: AWS (fully implemented), Azure (in progress), GCP (in progress)
- **Comprehensive Policy Analysis**: Scans IAM policies and resource-based policies across all supported services
- **Security Vulnerability Detection**: Identifies privilege escalation risks, wildcard permissions, and administrative access
- **Interactive CLI**: User-friendly command-line interface with rich formatting and progress indicators
- **Detailed Reporting**: Generates JSON reports with actionable findings and recommendations
- **Least Privilege Analysis**: Highlights violations of the principle of least privilege

## Supported AWS Services

- **IAM**: Customer managed policies, roles, users
- **S3**: Bucket policies
- **DynamoDB**: Table resource policies
- **Lambda**: Function resource policies
- **SNS**: Topic policies
- **SQS**: Queue policies
- **Glue**: Data catalog and database policies

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

**Need help with setup?** Check out the **[Installation Guide](https://thewintershadow.github.io/Lock-And-Key/installation.html)** for detailed instructions.

## Usage

### Interactive Mode

Run the interactive scanner to select providers and enter credentials:

```console
lock-and-key interactive
```

### Direct Scan Mode

Scan a specific provider with credentials:

```console
# AWS with profile
lock-and-key scan --provider AWS --profile my-profile

# AWS with access keys
lock-and-key scan --provider AWS --access-key YOUR_KEY --secret-key YOUR_SECRET --region us-east-1

# Azure (in progress)
lock-and-key scan --provider Azure --client-id YOUR_ID --secret YOUR_SECRET --tenant-id YOUR_TENANT

# GCP (in progress)
lock-and-key scan --provider GCP --creds-path /path/to/service-account.json
```

### Options

- `--output-dir`: Specify output directory for reports (default: `./reports`)
- `--provider`: Choose cloud provider (AWS, Azure, GCP)
- Various credential options for each provider

## Security Checks

Lock & Key identifies the following security issues:

- **Administrative Permissions**: Policies with `*:*` actions
- **Wildcard Resources**: Policies allowing access to all resources (`*`)
- **Privilege Escalation**: IAM permissions that could lead to privilege escalation
- **Overly Broad Access**: Resource policies with excessive permissions
- **Cross-Account Access**: Policies allowing external account access

## Report Format

Reports are generated in JSON format with the following structure:

```json
{
  "provider": "AWS",
  "account_id": "123456789012",
  "issues_found": 15,
  "least_privilege_violations": 8,
  "high_risk_permissions": 3,
  "summary": "Scanned IAM and all resource policies. Found 15 security issues.",
  "findings": [
    {
      "resource_name": "MyPolicy",
      "resource_id": "arn:aws:iam::123456789012:policy/MyPolicy",
      "issue_type": "Excessive Permissions",
      "severity": "High",
      "description": "Administrative permissions (*:*) detected",
      "recommendation": "Replace wildcard permissions with specific actions"
    }
  ]
}
```

## Documentation

📚 **[Complete Documentation](https://thewintershadow.github.io/Lock-And-Key/)**

- **[Installation Guide](https://thewintershadow.github.io/Lock-And-Key/installation.html)** - Detailed installation instructions and AWS setup
- **[Usage Guide](https://thewintershadow.github.io/Lock-And-Key/usage.html)** - Command-line examples and output interpretation
- **[API Reference](https://thewintershadow.github.io/Lock-And-Key/api.html)** - Complete API documentation
- **[Development Guide](https://thewintershadow.github.io/Lock-And-Key/development.html)** - Contributing and development setup

## Cloud Provider Status

- ✅ **AWS**: Fully implemented with comprehensive policy analysis
- 🚧 **Azure**: In progress  
- 🚧 **GCP**: In progress

## Development

For development setup, testing, and contributing guidelines, see the **[Development Guide](https://thewintershadow.github.io/Lock-And-Key/development.html)**.

### Quick Development Setup

```bash
git clone https://github.com/TheWinterShadow/lock-and-key.git
cd lock-and-key
hatch env create
hatch test
```

## License

`lock-and-key` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

