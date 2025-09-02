"""Base cloud provider interface."""

from abc import ABC, abstractmethod
from typing import Any

from ..models.scan_results import ScanResult


class CloudProviderBase(ABC):
    """Base class for cloud provider implementations."""

    name: str
    description: str

    @abstractmethod
    def prompt_creds(self) -> Any:
        """Prompt user for credentials."""
        pass

    def run_analysis(self, creds: Any) -> ScanResult:
        """Run security analysis for the provider."""
        # Placeholder implementation
        return ScanResult(
            provider=self.name,
            account_id="123456789012",
            issues_found=3,
            least_privilege_violations=2,
            high_risk_permissions=1,
            summary=f"Sample summary for {self.name}",
            report_path=f"./reports/{self.name.lower()}_report.json",
        )
