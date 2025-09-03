"""Unit tests for AWS S3 service."""

import unittest
from unittest.mock import Mock
from botocore.exceptions import ClientError

from lock_and_key.providers.aws.resources.s3 import S3Service


class TestS3Service(unittest.TestCase):
    """Test cases for S3Service class."""

    def setUp(self):
        """Set up test fixtures."""
        self.mock_session = Mock()
        self.service = S3Service(self.mock_session)

    def test_scan_policies_success(self):
        """Test successful S3 policy scanning."""
        mock_s3 = Mock()
        mock_s3.list_buckets.return_value = {"Buckets": [{"Name": "test-bucket"}]}
        mock_s3.get_bucket_policy.return_value = {
            "Policy": '{"Statement": [{"Principal": "*", "Action": "s3:GetObject", "Resource": "arn:aws:s3:::test-bucket/*"}]}'
        }
        self.mock_session.client.return_value = mock_s3
        
        issues = self.service.scan_policies("123456789012")
        
        self.assertGreater(len(issues), 0)
        self.assertTrue(any("External account access" in issue for issue in issues))

    def test_scan_policies_list_error(self):
        """Test S3 scanning with list buckets error."""
        mock_s3 = Mock()
        mock_s3.list_buckets.side_effect = ClientError({"Error": {"Code": "AccessDenied"}}, "ListBuckets")
        self.mock_session.client.return_value = mock_s3
        
        issues = self.service.scan_policies("123456789012")
        
        self.assertEqual(len(issues), 1)
        self.assertIn("Failed to list S3 buckets", issues[0])

    def test_has_external_access(self):
        """Test detection of external access."""
        # Test wildcard principal
        statement = {"Principal": "*"}
        self.assertTrue(self.service._has_external_access(statement, "123456789012"))
        
        # Test external account
        statement = {"Principal": {"AWS": "arn:aws:iam::999999999999:root"}}
        self.assertTrue(self.service._has_external_access(statement, "123456789012"))
        
        # Test same account
        statement = {"Principal": {"AWS": "arn:aws:iam::123456789012:root"}}
        self.assertFalse(self.service._has_external_access(statement, "123456789012"))

    def test_has_wildcard_permissions(self):
        """Test detection of wildcard permissions."""
        # Test wildcard action
        statement = {"Action": "s3:*", "Resource": "arn:aws:s3:::bucket/key"}
        self.assertTrue(self.service._has_wildcard_permissions(statement))
        
        # Test wildcard resource without conditions
        statement = {"Action": "s3:GetObject", "Resource": "arn:aws:s3:::bucket/*"}
        self.assertTrue(self.service._has_wildcard_permissions(statement))
        
        # Test specific permissions
        statement = {"Action": "s3:GetObject", "Resource": "arn:aws:s3:::bucket/key"}
        self.assertFalse(self.service._has_wildcard_permissions(statement))

    def test_missing_prefix_filter(self):
        """Test detection of missing prefix filters."""
        # Test broad action with wildcard resource, no conditions
        statement = {
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::bucket/*"
        }
        self.assertTrue(self.service._missing_prefix_filter(statement))
        
        # Test with prefix conditions
        statement = {
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::bucket/*",
            "Condition": {"StringLike": {"s3:prefix": "user/*"}}
        }
        self.assertFalse(self.service._missing_prefix_filter(statement))

    def test_has_prefix_conditions(self):
        """Test detection of prefix-based conditions."""
        # Test with prefix condition
        conditions = {"StringLike": {"s3:prefix": "user/*"}}
        self.assertTrue(self.service._has_prefix_conditions(conditions))
        
        # Test with key condition
        conditions = {"StringEquals": {"s3:ExistingObjectTag/key": "value"}}
        self.assertTrue(self.service._has_prefix_conditions(conditions))
        
        # Test without prefix conditions
        conditions = {"IpAddress": {"aws:SourceIp": "203.0.113.0/24"}}
        self.assertFalse(self.service._has_prefix_conditions(conditions))


if __name__ == '__main__':
    unittest.main()