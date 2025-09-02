"""Unit tests for lock_and_key.models.scan_results module."""

import unittest
from unittest.mock import Mock, patch

from lock_and_key.models.scan_results import ScanResult, ScanSummary


class TestScanResult(unittest.TestCase):
    """Test cases for ScanResult model."""

    def test_scan_result_creation(self):
        """Test ScanResult can be created with all fields."""
        result = ScanResult(
            provider="AWS",
            account_id="123456789012",
            issues_found=5,
            least_privilege_violations=3,
            high_risk_permissions=2,
            summary="Test summary",
            report_path="/path/to/report.json"
        )
        
        self.assertEqual(result.provider, "AWS")
        self.assertEqual(result.account_id, "123456789012")
        self.assertEqual(result.issues_found, 5)
        self.assertEqual(result.least_privilege_violations, 3)
        self.assertEqual(result.high_risk_permissions, 2)
        self.assertEqual(result.summary, "Test summary")
        self.assertEqual(result.report_path, "/path/to/report.json")

    def test_scan_result_validation(self):
        """Test ScanResult validates field types."""
        # Should work with valid data
        result = ScanResult(
            provider="GCP",
            account_id="test-project-123",
            issues_found=0,
            least_privilege_violations=0,
            high_risk_permissions=0,
            summary="No issues found",
            report_path="/reports/gcp_report.json"
        )
        self.assertIsInstance(result, ScanResult)

    def test_scan_result_equality(self):
        """Test ScanResult equality comparison."""
        result1 = ScanResult(
            provider="AWS",
            account_id="123456789012",
            issues_found=1,
            least_privilege_violations=1,
            high_risk_permissions=0,
            summary="Test",
            report_path="/test"
        )
        result2 = ScanResult(
            provider="AWS",
            account_id="123456789012",
            issues_found=1,
            least_privilege_violations=1,
            high_risk_permissions=0,
            summary="Test",
            report_path="/test"
        )
        
        self.assertEqual(result1, result2)


class TestScanSummary(unittest.TestCase):
    """Test cases for ScanSummary model."""

    def setUp(self):
        """Set up test fixtures."""
        self.summary = ScanSummary()
        self.sample_result = ScanResult(
            provider="AWS",
            account_id="123456789012",
            issues_found=3,
            least_privilege_violations=2,
            high_risk_permissions=1,
            summary="Sample result",
            report_path="/reports/aws_report.json"
        )

    def test_scan_summary_initialization(self):
        """Test ScanSummary initializes with empty results."""
        self.assertEqual(len(self.summary.results), 0)
        self.assertIsInstance(self.summary.results, list)

    def test_add_result(self):
        """Test adding a result to the summary."""
        self.summary.add_result(self.sample_result)
        
        self.assertEqual(len(self.summary.results), 1)
        self.assertEqual(self.summary.results[0], self.sample_result)

    def test_add_multiple_results(self):
        """Test adding multiple results to the summary."""
        result2 = ScanResult(
            provider="GCP",
            account_id="test-project",
            issues_found=1,
            least_privilege_violations=0,
            high_risk_permissions=1,
            summary="GCP result",
            report_path="/reports/gcp_report.json"
        )
        
        self.summary.add_result(self.sample_result)
        self.summary.add_result(result2)
        
        self.assertEqual(len(self.summary.results), 2)
        self.assertEqual(self.summary.results[0].provider, "AWS")
        self.assertEqual(self.summary.results[1].provider, "GCP")

    @patch('lock_and_key.models.scan_results.Console')
    def test_render_empty_summary(self, mock_console_class):
        """Test rendering empty summary."""
        mock_console = Mock()
        mock_console_class.return_value = mock_console
        
        self.summary.render()
        
        mock_console_class.assert_called_once()
        mock_console.print.assert_called_once()

    @patch('lock_and_key.models.scan_results.Console')
    @patch('lock_and_key.models.scan_results.Table')
    def test_render_with_results(self, mock_table_class, mock_console_class):
        """Test rendering summary with results."""
        mock_console = Mock()
        mock_table = Mock()
        mock_console_class.return_value = mock_console
        mock_table_class.return_value = mock_table
        
        self.summary.add_result(self.sample_result)
        self.summary.render()
        
        mock_console_class.assert_called_once()
        mock_table_class.assert_called_once_with(title="Scan Summary Report")
        
        # Verify table columns are added
        expected_columns = [
            "Provider", "Account ID", "Issues", "Least Privilege", 
            "High Risk", "Summary", "Report Path"
        ]
        self.assertEqual(mock_table.add_column.call_count, len(expected_columns))
        
        # Verify row is added for the result
        mock_table.add_row.assert_called_once_with(
            "AWS", "123456789012", "3", "2", "1", 
            "Sample result", "/reports/aws_report.json"
        )
        
        mock_console.print.assert_called_once_with(mock_table)

    def test_scan_summary_equality(self):
        """Test ScanSummary equality comparison."""
        summary1 = ScanSummary()
        summary2 = ScanSummary()
        
        summary1.add_result(self.sample_result)
        summary2.add_result(self.sample_result)
        
        self.assertEqual(summary1, summary2)


if __name__ == '__main__':
    unittest.main()