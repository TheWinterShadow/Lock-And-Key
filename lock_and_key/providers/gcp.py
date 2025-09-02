"""GCP provider implementation."""

import click

from ..models.credentials import GCPCreds
from .base import CloudProviderBase


class GCPProvider(CloudProviderBase):
    """GCP cloud provider implementation."""

    name = "GCP"
    description = "Google Cloud Platform"

    def prompt_creds(self) -> GCPCreds:
        """Prompt for GCP credentials."""
        creds_path = click.prompt(
            "Enter path to GCP service account JSON file (leave blank to paste JSON)",
            default="",
            show_default=False,
        )
        if creds_path:
            return GCPCreds(creds_path=creds_path)

        creds_json = click.prompt("Paste your GCP service account JSON")
        return GCPCreds(creds_json=creds_json)
