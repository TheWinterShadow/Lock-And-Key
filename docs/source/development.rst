Development
===========

This section covers development setup, contributing guidelines, and project structure.

Development Setup
-----------------

Prerequisites
~~~~~~~~~~~~~

- Python 3.9+
- Git
- Hatch (recommended) or pip

Clone and Setup
~~~~~~~~~~~~~~~

.. code-block:: console

   $ git clone https://github.com/TheWinterShadow/lock-and-key.git
   $ cd lock-and-key
   $ hatch env create

Running Tests
~~~~~~~~~~~~~

.. code-block:: console

   # Run all tests
   $ hatch test

   # Run tests with coverage
   $ hatch run test:cov

   # Run specific test files
   $ hatch test tests/test_cli.py

Code Quality
~~~~~~~~~~~~

.. code-block:: console

   # Format code
   $ hatch run dev:black .
   $ hatch run dev:isort .

   # Lint code
   $ hatch run dev:flake8 .
   $ hatch run dev:mypy .

   # Run all pre-build checks
   $ hatch run dev:pre-build

Building Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

   $ hatch run dev:docs

Project Structure
-----------------

.. code-block::

   lock_and_key/
   ├── __init__.py          # Package initialization
   ├── __about__.py         # Version information
   ├── cli.py               # Command-line interface
   ├── main.py              # Main entry point
   ├── config/              # Configuration settings
   │   ├── __init__.py
   │   └── settings.py
   ├── core/                # Core scanning logic
   │   ├── __init__.py
   │   ├── scanner.py       # Main scanner class
   │   └── ui.py            # User interface utilities
   ├── providers/           # Cloud provider implementations
   │   ├── __init__.py
   │   ├── azure.py         # Azure provider (in progress)
   │   ├── gcp.py           # GCP provider (in progress)
   │   └── aws/             # AWS provider implementation
   │       ├── __init__.py
   │       ├── aws_provider.py
   │       ├── aws_policy_collector.py
   │       └── resources/   # AWS service-specific modules
   │           ├── __init__.py
   │           ├── base.py
   │           └── iam.py
   └── types/               # Data models and types
       ├── __init__.py
       ├── base.py          # Base provider interface
       ├── credentials.py   # Credential models
       ├── exceptions.py    # Custom exceptions
       └── scan_results.py  # Result models

Contributing
------------

We welcome contributions! Please follow these guidelines:

Code Style
~~~~~~~~~~

- Use Black for code formatting
- Follow PEP 8 guidelines
- Add type hints to all functions
- Write docstrings for public APIs

Testing
~~~~~~~

- Write unit tests for new features
- Ensure all tests pass before submitting
- Aim for high test coverage
- Use meaningful test names and descriptions

Documentation
~~~~~~~~~~~~~

- Update documentation for new features
- Include examples in docstrings
- Follow Google-style docstring format

Pull Requests
~~~~~~~~~~~~~

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add/update tests
5. Update documentation
6. Run pre-build checks
7. Submit a pull request

Architecture
------------

Provider Interface
~~~~~~~~~~~~~~~~~~

All cloud providers implement the ``CloudProviderBase`` abstract class:

.. code-block:: python

   class CloudProviderBase(ABC):
       name: str
       description: str

       @abstractmethod
       def prompt_creds(self) -> Any:
           """Prompt user for credentials."""
           pass

       def run_analysis(self, creds: Any, output_dir: str = "./reports") -> ScanResult:
           """Run security analysis for the provider."""
           pass

Scanner Architecture
~~~~~~~~~~~~~~~~~~~~

The main ``LockAndKeyScanner`` class orchestrates the scanning process:

1. **Provider Selection**: User selects cloud provider
2. **Credential Collection**: Provider prompts for credentials
3. **Analysis Execution**: Provider runs security analysis
4. **Result Aggregation**: Results are collected and displayed
5. **Report Generation**: JSON reports are saved to disk

Adding New Providers
~~~~~~~~~~~~~~~~~~~~

To add support for a new cloud provider:

1. Create a new provider class inheriting from ``CloudProviderBase``
2. Implement the ``prompt_creds()`` method
3. Implement the ``run_analysis()`` method
4. Add credential model to ``types/credentials.py``
5. Register provider in ``providers/__init__.py``
6. Add tests in ``tests/providers/``

Release Process
---------------

1. Update version in ``lock_and_key/__about__.py``
2. Update CHANGELOG.md
3. Run all tests and quality checks
4. Create and push git tag
5. GitHub Actions will build and publish to PyPI

Environment Variables
---------------------

The following environment variables can be used:

``LOCK_AND_KEY_OUTPUT_DIR``
  Default output directory for reports

``LOCK_AND_KEY_LOG_LEVEL``
  Logging level (DEBUG, INFO, WARNING, ERROR)

``AWS_PROFILE``
  Default AWS profile to use

Debugging
---------

Enable debug logging:

.. code-block:: python

   import logging
   logging.basicConfig(level=logging.DEBUG)

Use the ``--verbose`` flag (if implemented) for detailed output.
