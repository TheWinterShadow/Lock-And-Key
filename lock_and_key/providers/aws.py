"""AWS provider implementation."""

import click

from lock_and_key.models.credentials import AWSCreds
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
