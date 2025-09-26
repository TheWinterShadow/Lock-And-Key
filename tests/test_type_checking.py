#!/usr/bin/env python3
"""Test script to verify TYPE_CHECKING behavior works correctly.

This script tests that the codebase can be imported and used without 
type stub dependencies, ensuring TYPE_CHECKING guards work properly.
"""

import sys
import importlib
from typing import List, Tuple


def test_imports_without_stubs() -> bool:
    """Test that all modules can be imported without type stubs."""
    modules_to_test = [
        "lock_and_key",
        "lock_and_key.cli", 
        "lock_and_key.core",
        "lock_and_key.core.scanner",
        "lock_and_key.providers.aws",
        "lock_and_key.providers.aws.aws_provider",
        "lock_and_key.providers.aws.aws_policy_collector",
        "lock_and_key.providers.aws.resources.iam",
        "lock_and_key.providers.aws.resources.base",
        "lock_and_key.types",
        "lock_and_key.types.scan_results",
    ]
    
    failed_imports: List[Tuple[str, str]] = []
    
    for module_name in modules_to_test:
        try:
            importlib.import_module(module_name)
            print(f"✅ {module_name}")
        except ImportError as e:
            print(f"❌ {module_name}: {e}")
            failed_imports.append((module_name, str(e)))
        except Exception as e:
            print(f"⚠️  {module_name}: {e}")
            failed_imports.append((module_name, str(e)))
    
    if failed_imports:
        print(f"\n❌ {len(failed_imports)} import(s) failed:")
        for module, error in failed_imports:
            print(f"  - {module}: {error}")
        return False
    else:
        print(f"\n✅ All {len(modules_to_test)} modules imported successfully!")
        return True


def test_cli_entrypoint() -> bool:
    """Test that the CLI entry point works."""
    try:
        from lock_and_key.cli import cli  # noqa: F401
        print("✅ CLI entry point accessible")
        return True
    except Exception as e:
        print(f"❌ CLI entry point failed: {e}")
        return False


def main() -> int:
    """Run all TYPE_CHECKING tests."""
    print("🔍 Testing TYPE_CHECKING behavior...")
    print("=" * 50)
    
    success = True
    
    # Test imports
    print("\n📦 Testing module imports:")
    success &= test_imports_without_stubs()
    
    # Test CLI
    print("\n🖥️  Testing CLI entry point:")
    success &= test_cli_entrypoint()
    
    # Summary
    print("\n" + "=" * 50)
    if success:
        print("🎉 All TYPE_CHECKING tests passed!")
        return 0
    else:
        print("💥 Some TYPE_CHECKING tests failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
