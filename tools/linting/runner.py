#!/usr/bin/env python3
import subprocess
import sys


def main():
    if len(sys.argv) < 3:
        print("Usage: runner.py <tool_name> <files...>")
        sys.exit(1)

    tool = sys.argv[1]
    files = sys.argv[2:]

    result = subprocess.run([tool, *files])
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
