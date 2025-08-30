import json
import pytest
from unittest.mock import patch, mock_open, MagicMock
from lock_and_key.modules.aws.base import AWS

# Dummy credentials for testing
DUMMY_CREDS = {"id": "dummy_id", "key": "dummy_key"}

class DummyAWS(AWS):
    """Concrete subclass for testing abstract AWS base class."""
    pass

@pytest.fixture
def mock_creds_file():
    m = mock_open(read_data=json.dumps(DUMMY_CREDS))
    with patch("builtins.open", m):
        yield

@pytest.fixture
def mock_boto3_session():
    with patch("lock_and_key.modules.aws.base.Session") as MockSession:
        mock_session = MagicMock()
        MockSession.return_value = mock_session
        yield mock_session

def test_get_creds_reads_key_json(mock_creds_file):
    aws = DummyAWS()
    creds = aws._get_creds()
    assert creds == DUMMY_CREDS

def test_create_session_uses_creds(mock_creds_file, mock_boto3_session):
    aws = DummyAWS()
    session = aws._create_session()
    assert session is mock_boto3_session
    mock_boto3_session.assert_not_called()  # Session is mocked, so just check instantiation

def test_post_init_sets_creds_and_session(mock_creds_file, mock_boto3_session):
    aws = DummyAWS()
    aws.__post_init__()
    assert aws.creds == DUMMY_CREDS
    assert aws.session is mock_boto3_session

def test_account_id_property_returns_account_id(mock_creds_file, mock_boto3_session):
    mock_client = MagicMock()
    mock_client.get_caller_identity.return_value = {"Account": "123456789012"}
    mock_boto3_session.client.return_value = mock_client
    aws = DummyAWS()
    aws.session = mock_boto3_session
    assert aws.account_id == "123456789012"
    mock_boto3_session.client.assert_called_with("sts")

def test_create_client_returns_boto3_client(mock_creds_file, mock_boto3_session):
    mock_client = MagicMock()
    mock_boto3_session.client.return_value = mock_client
    aws = DummyAWS()
    aws.session = mock_boto3_session
    client = aws.create_client("ec2")
    assert client is mock_client
    mock_boto3_session.client.assert_called_with("ec2")

def test_create_resource_returns_boto3_resource(mock_creds_file, mock_boto3_session):
    mock_resource = MagicMock()
    mock_boto3_session.resource.return_value = mock_resource
    aws = DummyAWS()
    aws.session = mock_boto3_session
    resource = aws.create_resource("s3")
    assert resource is mock_resource
    mock_boto3_session.resource.assert_called_with("s3")