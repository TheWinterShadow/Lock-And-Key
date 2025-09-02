"""Unit tests for lock_and_key.providers.aws module."""

import unittest
from unittest.mock import patch

from lock_and_key.models.credentials import AWSCreds
from lock_and_key.providers.aws import AWSProvider
from lock_and_key.providers.base import CloudProviderBase


class TestAWSProvider(unittest.TestCase):
    """Test cases for AWSProvider class."""

    def setUp(self):
        """Set up test fixtures."""
        self.provider = AWSProvider()

    def test_inheritance(self):
        """Test that AWSProvider inherits from CloudProviderBase."""
        self.assertIsInstance(self.provider, CloudProviderBase)

    def test_class_attributes(self):
        """Test AWSProvider class attributes."""
        self.assertEqual(self.provider.name, "AWS")
        self.assertEqual(self.provider.description, "Amazon Web Services")

    @patch('click.prompt')
    def test_prompt_creds_with_profile(self, mock_prompt):
        """Test prompting for credentials with AWS profile."""
        mock_prompt.return_value = "test-profile"
        
        creds = self.provider.prompt_creds()
        
        self.assertIsInstance(creds, AWSCreds)
        self.assertEqual(creds.profile, "test-profile")
        self.assertIsNone(creds.access_key)
        self.assertIsNone(creds.secret_key)
        self.assertIsNone(creds.region)
        
        # Should only prompt once for profile
        self.assertEqual(mock_prompt.call_count, 1)

    @patch('click.prompt')
    def test_prompt_creds_with_keys(self, mock_prompt):
        """Test prompting for credentials with access keys."""
        # First prompt returns empty string (no profile)
        # Then prompts for access key, secret key, and region
        mock_prompt.side_effect = ["", "AKIATEST123", "test-secret-key", "us-west-2"]
        
        creds = self.provider.prompt_creds()
        
        self.assertIsInstance(creds, AWSCreds)
        self.assertIsNone(creds.profile)
        self.assertEqual(creds.access_key, "AKIATEST123")
        self.assertEqual(creds.secret_key, "test-secret-key")
        self.assertEqual(creds.region, "us-west-2")
        
        # Should prompt 4 times: profile, access_key, secret_key, region
        self.assertEqual(mock_prompt.call_count, 4)

    @patch('click.prompt')
    def test_prompt_creds_default_region(self, mock_prompt):
        """Test that default region is us-east-1."""
        mock_prompt.side_effect = ["", "AKIATEST123", "test-secret-key", "us-east-1"]
        
        creds = self.provider.prompt_creds()
        
        self.assertEqual(creds.region, "us-east-1")
        
        # Verify the region prompt had the correct default
        region_call = mock_prompt.call_args_list[3]
        self.assertEqual(region_call[1]['default'], "us-east-1")

    @patch('click.prompt')
    def test_prompt_creds_hide_secret_input(self, mock_prompt):
        """Test that secret key input is hidden."""
        mock_prompt.side_effect = ["", "AKIATEST123", "test-secret-key", "us-east-1"]
        
        self.provider.prompt_creds()
        
        # Check that the secret key prompt has hide_input=True
        secret_call = mock_prompt.call_args_list[2]
        self.assertTrue(secret_call[1]['hide_input'])

    def test_run_analysis_inherited(self):
        """Test that run_analysis method is inherited from base class."""
        # This tests the inherited behavior
        creds = AWSCreds(profile="test-profile")
        result = self.provider.run_analysis(creds)
        
        self.assertEqual(result.provider, "AWS")
        self.assertIn("aws", result.report_path.lower())


if __name__ == '__main__':
    unittest.main()