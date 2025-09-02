"""Tests for the main scanner functionality."""
import pytest
from lock_and_key.core import LockAndKeyScanner
from lock_and_key.models import ScanResult


def test_scanner_initialization():
    """Test that scanner initializes correctly."""
    scanner = LockAndKeyScanner()
    assert scanner.providers is not None
    assert len(scanner.providers) == 3
    assert "AWS" in scanner.providers
    assert "GCP" in scanner.providers
    assert "Azure" in scanner.providers


def test_build_aws_credentials():
    """Test AWS credentials building."""
    scanner = LockAndKeyScanner()
    creds = scanner._build_credentials("AWS", profile="test-profile", region="us-west-2")
    assert creds.profile == "test-profile"
    assert creds.region == "us-west-2"


def test_build_invalid_provider_credentials():
    """Test invalid provider credentials."""
    scanner = LockAndKeyScanner()
    creds = scanner._build_credentials("INVALID", test="value")
    assert creds is None