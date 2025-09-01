import json
import unittest
from unittest.mock import Mock, mock_open, patch


class TestAWS(unittest.TestCase):
    def setUp(self):
        self.mock_creds = {"id": "test_access_key", "key": "test_secret_key"}

    @patch("lock_and_key.modules.aws.base.Session")
    @patch("lock_and_key.modules.aws.base.json.load")
    @patch("builtins.open", new_callable=mock_open)
    def test_init(self, mock_file, mock_json_load, mock_session_class):
        from lock_and_key.modules.aws.base import AWS

        mock_json_load.return_value = self.mock_creds
        mock_session_instance = Mock()
        mock_session_class.return_value = mock_session_instance

        AWS()

        mock_file.assert_called_once_with("key.json", "r")
        mock_json_load.assert_called_once()
        mock_session_class.assert_called_once_with(
            aws_access_key_id="test_access_key", aws_secret_access_key="test_secret_key"
        )

    @patch("lock_and_key.modules.aws.base.Session")
    @patch("lock_and_key.modules.aws.base.json.load")
    @patch("builtins.open", new_callable=mock_open)
    def test_creds_property(self, mock_file, mock_json_load, mock_session_class):
        from lock_and_key.modules.aws.base import AWS

        mock_json_load.return_value = self.mock_creds
        aws = AWS()

        self.assertEqual(aws.creds, self.mock_creds)

    @patch("lock_and_key.modules.aws.base.Session")
    @patch("lock_and_key.modules.aws.base.json.load")
    @patch("builtins.open", new_callable=mock_open)
    def test_session_property(self, mock_file, mock_json_load, mock_session_class):
        from lock_and_key.modules.aws.base import AWS

        mock_json_load.return_value = self.mock_creds
        mock_session_instance = Mock()
        mock_session_class.return_value = mock_session_instance

        aws = AWS()

        self.assertEqual(aws.session, mock_session_instance)

    @patch("lock_and_key.modules.aws.base.Session")
    @patch("lock_and_key.modules.aws.base.json.load")
    @patch("builtins.open", new_callable=mock_open)
    def test_account_id_property(self, mock_file, mock_json_load, mock_session_class):
        from lock_and_key.modules.aws.base import AWS

        mock_json_load.return_value = self.mock_creds
        mock_session_instance = Mock()
        mock_sts_client = Mock()
        mock_sts_client.get_caller_identity.return_value = {"Account": "123456789012"}
        mock_session_instance.client.return_value = mock_sts_client
        mock_session_class.return_value = mock_session_instance

        aws = AWS()

        self.assertEqual(aws.account_id, "123456789012")
        mock_session_instance.client.assert_called_with("sts")

    @patch("lock_and_key.modules.aws.base.Session")
    @patch("lock_and_key.modules.aws.base.json.load")
    @patch("builtins.open", new_callable=mock_open)
    def test_create_client(self, mock_file, mock_json_load, mock_session_class):
        from lock_and_key.modules.aws.base import AWS

        mock_json_load.return_value = self.mock_creds
        mock_session_instance = Mock()
        mock_client = Mock()
        mock_session_instance.client.return_value = mock_client
        mock_session_class.return_value = mock_session_instance

        aws = AWS()
        result = aws.create_client("s3")

        self.assertEqual(result, mock_client)
        mock_session_instance.client.assert_called_with("s3")

    @patch("lock_and_key.modules.aws.base.Session")
    @patch("lock_and_key.modules.aws.base.json.load")
    @patch("builtins.open", new_callable=mock_open)
    def test_create_resource(self, mock_file, mock_json_load, mock_session_class):
        from lock_and_key.modules.aws.base import AWS

        mock_json_load.return_value = self.mock_creds
        mock_session_instance = Mock()
        mock_resource = Mock()
        mock_session_instance.resource.return_value = mock_resource
        mock_session_class.return_value = mock_session_instance

        aws = AWS()
        result = aws.create_resource("s3")

        self.assertEqual(result, mock_resource)
        mock_session_instance.resource.assert_called_with("s3")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_get_creds_file_not_found(self, mock_file):
        from lock_and_key.modules.aws.base import AWS

        with self.assertRaises(FileNotFoundError):
            AWS()

    @patch("builtins.open", new_callable=mock_open, read_data="invalid json")
    @patch(
        "lock_and_key.modules.aws.base.json.load",
        side_effect=json.JSONDecodeError("msg", "doc", 0),
    )
    def test_get_creds_invalid_json(self, mock_json_load, mock_file):
        from lock_and_key.modules.aws.base import AWS

        with self.assertRaises(json.JSONDecodeError):
            AWS()


if __name__ == "__main__":
    unittest.main()
