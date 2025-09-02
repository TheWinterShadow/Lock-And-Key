"""Cloud provider implementations."""

from .aws import AWSProvider
from .azure import AzureProvider
from .base import CloudProviderBase
from .gcp import GCPProvider

PROVIDER_CLASSES = {"AWS": AWSProvider, "GCP": GCPProvider, "Azure": AzureProvider}

__all__ = [
    "CloudProviderBase",
    "AWSProvider",
    "GCPProvider",
    "AzureProvider",
    "PROVIDER_CLASSES",
]
