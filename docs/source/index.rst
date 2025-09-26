Lock & Key Documentation
========================

**Lock & Key** is a comprehensive cloud security scanner that analyzes access policies and resource-based policies across multiple cloud providers to identify security vulnerabilities, excessive permissions, and compliance issues.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api
   development

Features
--------

- **Multi-Cloud Support**: AWS (fully implemented), Azure (in progress), GCP (in progress)
- **Comprehensive Policy Analysis**: Scans IAM policies and resource-based policies across all supported services
- **Security Vulnerability Detection**: Identifies privilege escalation risks, wildcard permissions, and administrative access
- **Interactive CLI**: User-friendly command-line interface with rich formatting and progress indicators
- **Detailed Reporting**: Generates JSON reports with actionable findings and recommendations
- **Least Privilege Analysis**: Highlights violations of the principle of least privilege

Supported AWS Services
----------------------

- **IAM**: Customer managed policies, roles, users
- **S3**: Bucket policies
- **DynamoDB**: Resource policies
- **Lambda**: Function policies
- **SNS**: Topic policies
- **SQS**: Queue policies
- **Glue**: Resource policies

Quick Start
-----------

Install Lock & Key:

.. code-block:: console

   $ pip install lock-and-key

Run an interactive scan:

.. code-block:: console

   $ lock-and-key interactive

Or scan a specific provider:

.. code-block:: console

   $ lock-and-key scan --provider AWS --profile my-profile

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
