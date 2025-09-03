"""AWS provider implementation."""

import click
from botocore.exceptions import ClientError, NoCredentialsError

from lock_and_key.models.credentials import AWSCreds
from lock_and_key.models.scan_results import ScanResult
from lock_and_key.providers.aws.resources.iam import IAMService
from lock_and_key.providers.aws.resources.s3 import S3Service
from lock_and_key.providers.base import CloudProviderBase


class AWSProvider(CloudProviderBase):
    """AWS cloud provider implementation."""

    name = "AWS"
    description = "Amazon Web Services"

    def prompt_creds(self) -> AWSCreds:
        """Prompt for AWS credentials."""
        profile = click.prompt(
            "Enter AWS profile name (leave blank to enter keys)",
            default="",
            show_default=False,
        )
        if profile:
            return AWSCreds(profile=profile)

        access_key = click.prompt("Enter AWS Access Key ID")
        secret_key = click.prompt("Enter AWS Secret Access Key", hide_input=True)
        region = click.prompt("Enter AWS Region", default="us-east-1")

        return AWSCreds(access_key=access_key, secret_key=secret_key, region=region)

    def run_analysis(self, creds: AWSCreds, output_dir: str = "./reports") -> ScanResult:
        """Run AWS security analysis for S3 and IAM policies."""
        try:
            # Initialize services
            iam_service = IAMService.from_creds(creds)
            s3_service = S3Service.from_creds(creds)

            account_id = iam_service.get_account_id()

            # Scan both IAM and S3 policies
            iam_findings = iam_service.scan_policies_detailed(account_id)
            s3_findings = s3_service.scan_policies_detailed(account_id)

            all_findings = iam_findings + s3_findings

            return ScanResult(
                provider=self.name,
                account_id=account_id,
                issues_found=len(all_findings),
                least_privilege_violations=sum(
                    1 for f in all_findings if "wildcard" in f.description.lower() or "Administrative" in f.description
                ),
                high_risk_permissions=sum(1 for f in all_findings if f.severity == "High"),
                summary=f"Scanned IAM and S3 policies. Found {len(all_findings)} security issues.",
                report_path=f"{output_dir}/aws_report_{account_id}.json",
                findings=all_findings,
            )

        except (NoCredentialsError, ClientError) as e:
            return ScanResult(
                provider=self.name,
                account_id="unknown",
                issues_found=0,
                least_privilege_violations=0,
                high_risk_permissions=0,
                summary=f"Failed to scan AWS: {str(e)}",
                report_path="",
            )
