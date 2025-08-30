load("@rules_python//python:defs.bzl", "py_test")

py_test(
    name = "__init__",
    srcs = glob(
        [
            "test_*.py",
            "*_test.py",
            "__init__.py",
        ],
        allow_empty = True,
    ),
    deps = ["//lock_and_key:lock_and_key_lib"],
)
