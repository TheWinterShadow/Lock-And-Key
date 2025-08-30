# Initialize Bazel workspace for Python
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# Fetch Bazel Python rules
http_archive(
    name = "rules_python",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.31.0/rules_python-0.31.0.tar.gz",
    sha256 = "c3e6e2e63bf7b66b74fd9f5bff1f3f954ed7be35d8aacbb44e0c30b334c06c14",
)

load("@rules_python//python:repositories.bzl", "py_repositories")
py_repositories()