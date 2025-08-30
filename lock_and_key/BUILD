load("@rules_python//python:defs.bzl", "py_library", "py_binary")

filegroup(
    name = "all_py_files",
    srcs = glob(["**/*.py"]),
    visibility = ["//visibility:public"],
)

py_library(
    name = "lock_and_key_lib",
    srcs = glob(["**/*.py"]),
    imports = ["boto3", "pydantic", "mypy-boto3-iam"],
    visibility = ["//visibility:public"],
)

py_binary(
    name = "cli",
    srcs = glob(["*.py"]),
    main = "cli.py",
    deps = [":lock_and_key_lib"],
)
