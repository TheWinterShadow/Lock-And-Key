"""Data models for Lock & Key."""

from .credentials import AWSCreds, AzureCreds, GCPCreds
from .scan_results import ScanResult, ScanSummary

__all__ = ["AWSCreds", "GCPCreds", "AzureCreds", "ScanResult", "ScanSummary"]
