"""Scan result models."""

from typing import List

from pydantic import BaseModel
from rich.console import Console
from rich.table import Table


class ScanResult(BaseModel):
    """Result of a cloud provider scan."""

    provider: str
    account_id: str
    issues_found: int
    least_privilege_violations: int
    high_risk_permissions: int
    summary: str
    report_path: str


class ScanSummary(BaseModel):
    """Summary of all scan results."""

    results: List[ScanResult] = []

    def add_result(self, result: ScanResult) -> None:
        """Add a scan result to the summary."""
        self.results.append(result)

    def render(self) -> None:
        """Render the scan summary as a table."""
        console = Console()
        table = Table(title="Scan Summary Report")
        table.add_column("Provider", style="cyan", no_wrap=True)
        table.add_column("Account ID", style="magenta")
        table.add_column("Issues", style="red")
        table.add_column("Least Privilege", style="yellow")
        table.add_column("High Risk", style="red")
        table.add_column("Summary", style="green")
        table.add_column("Report Path", style="blue")

        for result in self.results:
            table.add_row(
                result.provider,
                result.account_id,
                str(result.issues_found),
                str(result.least_privilege_violations),
                str(result.high_risk_permissions),
                result.summary,
                result.report_path,
            )
        console.print(table)
