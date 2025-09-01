#!/usr/bin/env python3
import sys

import pytest

if __name__ == "__main__":
    sys.exit(pytest.main(["-v", "lock_and_key/tests/models/aws/test_base.py"]))
