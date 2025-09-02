"""Unit tests for lock_and_key.exceptions.base module."""

import unittest

from lock_and_key.exceptions.base import CredentialsError, LockAndKeyError, ProviderError


class TestExceptions(unittest.TestCase):
    """Test cases for exception classes."""

    def test_lock_and_key_error_inheritance(self):
        """Test that LockAndKeyError inherits from Exception."""
        self.assertTrue(issubclass(LockAndKeyError, Exception))

    def test_provider_error_inheritance(self):
        """Test that ProviderError inherits from LockAndKeyError."""
        self.assertTrue(issubclass(ProviderError, LockAndKeyError))
        self.assertTrue(issubclass(ProviderError, Exception))

    def test_credentials_error_inheritance(self):
        """Test that CredentialsError inherits from LockAndKeyError."""
        self.assertTrue(issubclass(CredentialsError, LockAndKeyError))
        self.assertTrue(issubclass(CredentialsError, Exception))

    def test_lock_and_key_error_instantiation(self):
        """Test LockAndKeyError can be instantiated and raised."""
        error = LockAndKeyError("Test error")
        self.assertEqual(str(error), "Test error")
        
        with self.assertRaises(LockAndKeyError):
            raise error

    def test_provider_error_instantiation(self):
        """Test ProviderError can be instantiated and raised."""
        error = ProviderError("Provider test error")
        self.assertEqual(str(error), "Provider test error")
        
        with self.assertRaises(ProviderError):
            raise error
        
        # Should also catch as base exception
        with self.assertRaises(LockAndKeyError):
            raise ProviderError("Another error")

    def test_credentials_error_instantiation(self):
        """Test CredentialsError can be instantiated and raised."""
        error = CredentialsError("Credentials test error")
        self.assertEqual(str(error), "Credentials test error")
        
        with self.assertRaises(CredentialsError):
            raise error
        
        # Should also catch as base exception
        with self.assertRaises(LockAndKeyError):
            raise CredentialsError("Another error")


if __name__ == '__main__':
    unittest.main()