Usage
=====

Lock & Key provides both interactive and command-line interfaces for scanning cloud environments.

Interactive Mode
----------------

The interactive mode guides you through the scanning process:

.. code-block:: console

   $ lock-and-key interactive

This will:

1. Prompt you to select a cloud provider
2. Ask for credentials (profile, keys, etc.)
3. Confirm before scanning
4. Display real-time progress
5. Show a summary of findings
6. Offer to scan additional providers

Direct Scan Mode
----------------

You can also run direct scans with specific parameters:

AWS Examples
~~~~~~~~~~~~

Using AWS profile:

.. code-block:: console

   $ lock-and-key scan --provider AWS --profile my-profile

Using access keys:

.. code-block:: console

   $ lock-and-key scan --provider AWS \\
     --access-key YOUR_ACCESS_KEY \\
     --secret-key YOUR_SECRET_KEY \\
     --region us-east-1

Azure Examples (In Progress)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

   $ lock-and-key scan --provider Azure \\
     --client-id YOUR_CLIENT_ID \\
     --secret YOUR_CLIENT_SECRET \\
     --tenant-id YOUR_TENANT_ID \\
     --subscription-id YOUR_SUBSCRIPTION_ID

GCP Examples (In Progress)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Using service account file:

.. code-block:: console

   $ lock-and-key scan --provider GCP \\
     --creds-path /path/to/service-account.json

Using JSON credentials:

.. code-block:: console

   $ lock-and-key scan --provider GCP \\
     --creds-json '{"type": "service_account", ...}'

Command Options
---------------

Global Options
~~~~~~~~~~~~~~

``--output-dir``
  Specify output directory for reports (default: ``./reports``)

AWS Options
~~~~~~~~~~~

``--profile``
  AWS profile name from ~/.aws/credentials

``--access-key``
  AWS Access Key ID

``--secret-key``
  AWS Secret Access Key

``--region``
  AWS Region (default: us-east-1)

Azure Options
~~~~~~~~~~~~~

``--creds-path``
  Path to Azure credentials file

``--client-id``
  Azure Client ID

``--secret``
  Azure Client Secret

``--tenant-id``
  Azure Tenant ID

``--subscription-id``
  Azure Subscription ID

GCP Options
~~~~~~~~~~~

``--creds-path``
  Path to GCP service account JSON file

``--creds-json``
  GCP service account JSON content

Understanding Output
--------------------

Lock & Key generates detailed JSON reports with:

- **Account Information**: Provider, account ID
- **Summary Statistics**: Total issues, privilege violations, high-risk permissions
- **Detailed Findings**: Individual security issues with descriptions and recommendations
- **Report Metadata**: Scan timestamp, file paths

Example output:

.. code-block:: json

   {
     "provider": "AWS",
     "account_id": "123456789012",
     "issues_found": 15,
     "least_privilege_violations": 8,
     "high_risk_permissions": 3,
     "summary": "Scanned IAM and all resource policies. Found 15 security issues.",
     "report_path": "./reports/aws_report_123456789012.json",
     "findings": [
       {
         "resource_name": "example-bucket",
         "resource_id": "arn:aws:s3:::example-bucket",
         "issue_type": "Overly Permissive Policy",
         "severity": "High",
         "description": "Bucket policy allows wildcard (*) access",
         "recommendation": "Restrict policy to specific principals"
       }
     ]
   }

Common Issues Detected
----------------------

**Wildcard Permissions**
  Policies using ``*`` for actions, resources, or principals

**Administrative Access**
  Policies granting broad administrative permissions

**Public Access**
  Resources accessible to the public internet

**Cross-Account Access**
  Resources accessible from external AWS accounts

**Privilege Escalation**
  Permissions that could lead to privilege escalation

**Unused Permissions**
  Overly broad permissions not following least privilege
