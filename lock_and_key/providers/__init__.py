"""Cloud provider implementations."""

from typing import Dict, Type

from lock_and_key.providers.aws import AWSProvider
from lock_and_key.providers.azure import AzureProvider
from lock_and_key.providers.base import CloudProviderBase
from lock_and_key.providers.gcp import GCPProvider

PROVIDER_CLASSES: Dict[str, Type[CloudProviderBase]] = {
    "AWS": AWSProvider,
    "GCP": GCPProvider,
    "Azure": AzureProvider,
}

__all__ = [
    "CloudProviderBase",
    "AWSProvider",
    "GCPProvider",
    "AzureProvider",
    "PROVIDER_CLASSES",
]
