Installation
============

Requirements
------------

- Python 3.9+
- boto3 (for AWS support)
- click (CLI framework)
- rich (terminal formatting)
- pydantic (data validation)

Install from PyPI
-----------------

.. code-block:: console

   $ pip install lock-and-key

Install from Source
-------------------

.. code-block:: console

   $ git clone https://github.com/TheWinterShadow/lock-and-key.git
   $ cd lock-and-key
   $ pip install -e .

Development Installation
------------------------

For development, use Hatch:

.. code-block:: console

   $ git clone https://github.com/TheWinterShadow/lock-and-key.git
   $ cd lock-and-key
   $ hatch env create

This will create a virtual environment with all dependencies installed.

AWS Configuration
-----------------

Lock & Key uses boto3 for AWS access. Configure your AWS credentials using:

1. AWS CLI: ``aws configure``
2. Environment variables: ``AWS_ACCESS_KEY_ID`` and ``AWS_SECRET_ACCESS_KEY``
3. IAM roles (for EC2 instances)
4. AWS credentials file

Required AWS Permissions
------------------------

Lock & Key requires read-only permissions for the following services:

- IAM (policies, roles, users)
- S3 (bucket policies)
- DynamoDB (resource policies)
- Lambda (function policies)
- SNS (topic policies)
- SQS (queue policies)
- Glue (resource policies)
- STS (for account information)

You can use the ``ReadOnlyAccess`` managed policy, or create a custom policy with specific permissions.
