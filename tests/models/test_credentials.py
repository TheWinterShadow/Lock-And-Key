"""Unit tests for lock_and_key.models.credentials module."""

import unittest

from lock_and_key.models.credentials import AWSCreds, AzureCreds, GCPCreds


class TestAWSCreds(unittest.TestCase):
    """Test cases for AWSCreds dataclass."""

    def test_aws_creds_default_values(self):
        """Test AWSCreds with default values."""
        creds = AWSCreds()
        self.assertIsNone(creds.profile)
        self.assertIsNone(creds.access_key)
        self.assertIsNone(creds.secret_key)
        self.assertIsNone(creds.region)

    def test_aws_creds_with_profile(self):
        """Test AWSCreds with profile."""
        creds = AWSCreds(profile="test-profile")
        self.assertEqual(creds.profile, "test-profile")
        self.assertIsNone(creds.access_key)
        self.assertIsNone(creds.secret_key)
        self.assertIsNone(creds.region)

    def test_aws_creds_with_keys(self):
        """Test AWSCreds with access keys."""
        creds = AWSCreds(
            access_key="AKIATEST",
            secret_key="test-secret",
            region="us-west-2"
        )
        self.assertIsNone(creds.profile)
        self.assertEqual(creds.access_key, "AKIATEST")
        self.assertEqual(creds.secret_key, "test-secret")
        self.assertEqual(creds.region, "us-west-2")

    def test_aws_creds_equality(self):
        """Test AWSCreds equality comparison."""
        creds1 = AWSCreds(profile="test")
        creds2 = AWSCreds(profile="test")
        creds3 = AWSCreds(profile="different")
        
        self.assertEqual(creds1, creds2)
        self.assertNotEqual(creds1, creds3)


class TestGCPCreds(unittest.TestCase):
    """Test cases for GCPCreds dataclass."""

    def test_gcp_creds_default_values(self):
        """Test GCPCreds with default values."""
        creds = GCPCreds()
        self.assertIsNone(creds.creds_path)
        self.assertIsNone(creds.creds_json)

    def test_gcp_creds_with_path(self):
        """Test GCPCreds with credentials path."""
        creds = GCPCreds(creds_path="/path/to/creds.json")
        self.assertEqual(creds.creds_path, "/path/to/creds.json")
        self.assertIsNone(creds.creds_json)

    def test_gcp_creds_with_json(self):
        """Test GCPCreds with JSON credentials."""
        json_creds = '{"type": "service_account"}'
        creds = GCPCreds(creds_json=json_creds)
        self.assertIsNone(creds.creds_path)
        self.assertEqual(creds.creds_json, json_creds)

    def test_gcp_creds_equality(self):
        """Test GCPCreds equality comparison."""
        creds1 = GCPCreds(creds_path="/test/path")
        creds2 = GCPCreds(creds_path="/test/path")
        creds3 = GCPCreds(creds_path="/different/path")
        
        self.assertEqual(creds1, creds2)
        self.assertNotEqual(creds1, creds3)


class TestAzureCreds(unittest.TestCase):
    """Test cases for AzureCreds dataclass."""

    def test_azure_creds_default_values(self):
        """Test AzureCreds with default values."""
        creds = AzureCreds()
        self.assertIsNone(creds.creds_path)
        self.assertIsNone(creds.client_id)
        self.assertIsNone(creds.secret)
        self.assertIsNone(creds.tenant_id)
        self.assertIsNone(creds.subscription_id)

    def test_azure_creds_with_path(self):
        """Test AzureCreds with credentials path."""
        creds = AzureCreds(creds_path="/path/to/azure/creds")
        self.assertEqual(creds.creds_path, "/path/to/azure/creds")
        self.assertIsNone(creds.client_id)

    def test_azure_creds_with_manual_values(self):
        """Test AzureCreds with manual credential values."""
        creds = AzureCreds(
            client_id="test-client-id",
            secret="test-secret",
            tenant_id="test-tenant-id",
            subscription_id="test-subscription-id"
        )
        self.assertIsNone(creds.creds_path)
        self.assertEqual(creds.client_id, "test-client-id")
        self.assertEqual(creds.secret, "test-secret")
        self.assertEqual(creds.tenant_id, "test-tenant-id")
        self.assertEqual(creds.subscription_id, "test-subscription-id")

    def test_azure_creds_equality(self):
        """Test AzureCreds equality comparison."""
        creds1 = AzureCreds(client_id="test-id")
        creds2 = AzureCreds(client_id="test-id")
        creds3 = AzureCreds(client_id="different-id")
        
        self.assertEqual(creds1, creds2)
        self.assertNotEqual(creds1, creds3)


if __name__ == '__main__':
    unittest.main()