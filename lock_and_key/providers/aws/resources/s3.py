"""AWS S3 policy scanner."""

import json
from typing import Any, Dict, List

from botocore.exceptions import ClientError
from mypy_boto3_s3 import S3Client

from lock_and_key.models.scan_results import Finding
from lock_and_key.providers.aws.resources.base import AWSServiceBase


class S3Service(AWSServiceBase):
    """AWS S3 service for bucket policy analysis."""

    def scan_policies(self, account_id: str) -> List[str]:
        """Scan S3 bucket policies for security issues."""
        issues: List[str] = []
        s3: S3Client = self.session.client("s3")

        try:
            buckets = s3.list_buckets()["Buckets"]

            for bucket in buckets:
                bucket_name = bucket.get("Name", "MISSING")
                bucket_issues = self._analyze_bucket_policy(s3, bucket_name, account_id)
                issues.extend(bucket_issues)

        except ClientError:
            issues.append("Failed to list S3 buckets")

        return issues

    def scan_policies_detailed(self, account_id: str) -> List[Finding]:
        """Scan S3 bucket policies and return detailed findings."""
        findings: List[Finding] = []
        s3: S3Client = self.session.client("s3")

        try:
            buckets = s3.list_buckets()["Buckets"]

            for bucket in buckets:
                bucket_name = bucket.get("Name", "MISSING")
                bucket_findings = self._analyze_bucket_policy_detailed(s3, bucket_name, account_id)
                findings.extend(bucket_findings)

        except ClientError:
            findings.append(
                Finding(
                    resource_name="S3 Buckets",
                    resource_id="N/A",
                    issue_type="Access Error",
                    severity="Medium",
                    description="Failed to list S3 buckets",
                    recommendation="Ensure S3 permissions allow bucket listing",
                )
            )

        return findings

    def _analyze_bucket_policy(self, s3: Any, bucket_name: str, account_id: str) -> List[str]:
        """Analyze individual bucket policy for security issues."""
        issues: List[str] = []

        try:
            policy_response = s3.get_bucket_policy(Bucket=bucket_name)
            policy = json.loads(policy_response["Policy"])

            for statement in policy.get("Statement", []):
                # Check for external account access
                if self._has_external_access(statement, account_id):
                    issues.append(f"Bucket {bucket_name}: External account access detected")

                # Check for wildcard permissions
                if self._has_wildcard_permissions(statement):
                    issues.append(f"Bucket {bucket_name}: Wildcard permissions (*) detected")

                # Check for missing prefix filters
                if self._missing_prefix_filter(statement):
                    issues.append(f"Bucket {bucket_name}: Missing prefix filter for broad permissions")

        except ClientError as e:
            if e.response["Error"]["Code"] != "NoSuchBucketPolicy":
                issues.append(f"Bucket {bucket_name}: Failed to retrieve policy")

        return issues

    def _has_external_access(self, statement: Dict[str, Any], account_id: str) -> bool:
        """Check if statement allows external account access."""
        principals = statement.get("Principal", {})

        if principals == "*":
            return True

        if isinstance(principals, dict):
            aws_principals = principals.get("AWS", [])
            if isinstance(aws_principals, str):
                aws_principals = [aws_principals]

            for principal in aws_principals:
                if principal == "*":
                    return True
                if isinstance(principal, str) and account_id not in principal:
                    return True

        return False

    def _has_wildcard_permissions(self, statement: Dict[str, Any]) -> bool:
        """Check if statement uses wildcard permissions."""
        actions = statement.get("Action", [])
        resources = statement.get("Resource", [])

        if isinstance(actions, str):
            actions = [actions]
        if isinstance(resources, str):
            resources = [resources]

        # Check for wildcard actions
        for action in actions:
            if "*" in action:
                return True

        # Check for wildcard resources
        for resource in resources:
            if resource.endswith("/*") and not self._has_condition_constraints(statement):
                return True

        return False

    def _missing_prefix_filter(self, statement: Dict[str, Any]) -> bool:
        """Check if statement is missing prefix filter for broad permissions."""
        actions = statement.get("Action", [])
        resources = statement.get("Resource", [])
        conditions = statement.get("Condition", {})

        if isinstance(actions, str):
            actions = [actions]
        if isinstance(resources, str):
            resources = [resources]

        # Check for broad object access without prefix constraints
        broad_actions = ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"]
        has_broad_action = any(action in broad_actions or "*" in action for action in actions)
        has_wildcard_resource = any(resource.endswith("/*") for resource in resources)

        if has_broad_action and has_wildcard_resource:
            # Check if there are prefix-based conditions
            return not self._has_prefix_conditions(conditions)

        return False

    def _has_condition_constraints(self, statement: Dict[str, Any]) -> bool:
        """Check if statement has meaningful condition constraints."""
        conditions = statement.get("Condition", {})
        return bool(conditions)

    def _has_prefix_conditions(self, conditions: Dict[str, Any]) -> bool:
        """Check if conditions include prefix-based restrictions."""
        for condition_type, condition_values in conditions.items():
            if isinstance(condition_values, dict):
                for key in condition_values.keys():
                    if "prefix" in key.lower() or "key" in key.lower():
                        return True
        return False

    def _analyze_bucket_policy_detailed(self, s3: Any, bucket_name: str, account_id: str) -> List[Finding]:
        """Analyze individual bucket policy and return detailed findings."""
        findings: List[Finding] = []

        try:
            policy_response = s3.get_bucket_policy(Bucket=bucket_name)
            policy = json.loads(policy_response["Policy"])

            for statement in policy.get("Statement", []):
                if self._has_external_access(statement, account_id):
                    findings.append(
                        Finding(
                            resource_name=bucket_name,
                            resource_id=f"arn:aws:s3:::{bucket_name}",
                            issue_type="External Access",
                            severity="High",
                            description="External account access detected",
                            recommendation="Restrict access to trusted accounts only",
                        )
                    )

                if self._has_wildcard_permissions(statement):
                    findings.append(
                        Finding(
                            resource_name=bucket_name,
                            resource_id=f"arn:aws:s3:::{bucket_name}",
                            issue_type="Overly Broad Access",
                            severity="Medium",
                            description="Wildcard permissions (*) detected",
                            recommendation="Use specific actions and resource paths",
                        )
                    )

                if self._missing_prefix_filter(statement):
                    findings.append(
                        Finding(
                            resource_name=bucket_name,
                            resource_id=f"arn:aws:s3:::{bucket_name}",
                            issue_type="Missing Access Control",
                            severity="Medium",
                            description="Missing prefix filter for broad permissions",
                            recommendation="Add prefix-based conditions to limit access scope",
                        )
                    )

        except ClientError as e:
            if e.response["Error"]["Code"] != "NoSuchBucketPolicy":
                findings.append(
                    Finding(
                        resource_name=bucket_name,
                        resource_id=f"arn:aws:s3:::{bucket_name}",
                        issue_type="Access Error",
                        severity="Low",
                        description="Failed to retrieve policy",
                        recommendation="Ensure S3 permissions allow policy access",
                    )
                )

        return findings
