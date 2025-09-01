load("@rules_python//python:defs.bzl", "py_binary")

def _make_lint_check(name, entry_point, deps):
    py_binary(
        name = name + "_runner",
        srcs = ["//tools/linting:runner.py"],
        deps = deps,
        main = "//tools/linting:runner.py",
    )

    if entry_point == "black":
        cmd_command = "$(location :{}_runner) {} $(locations //lock_and_key:all_py_files) 2>&1 | head -50 | tee $@ || (echo 'Black Linting failed' && exit 1)".format(name, entry_point)
    elif entry_point == "isort":
        cmd_command = "$(location :{}_runner) {} $(locations //lock_and_key:all_py_files) 2>&1 | head -50 | tee $@ || (echo 'ISort Linting failed' && exit 1)".format(name, entry_point)
    elif entry_point == "flake8":
        cmd_command = "$(location :{}_runner) {} $(locations //lock_and_key:all_py_files) --max-line-length 120 2>&1 | head -50 | tee $@ || (echo 'Flake8 Linting failed' && exit 1)".format(name, entry_point)
    elif entry_point == "mypy":
        cmd_command = "$(location :{}_runner) {} $(locations //lock_and_key:all_py_files) 2>&1 | head -50 | tee $@ || (echo 'Mypy Linting failed' && exit 1)".format(name, entry_point)
    else:
        fail("Unsupported linter: {}".format(entry_point))
    
    native.genrule(
        name = name + "_check",
        srcs = ["//lock_and_key:all_py_files"],
        outs = [name + "_report.txt"],
        cmd = cmd_command,
        tools = [":" + name + "_runner"],
    )

def black_lint(name = "black", deps = None):
    _make_lint_check(name, "black", deps or ["@pip//black"])

def isort_lint(name = "isort", deps = None):
    _make_lint_check(name, "isort", deps or ["@pip//isort"])

def flake8_lint(name = "flake8", deps = None):
    _make_lint_check(name, "flake8", deps or ["@pip//flake8"])

def mypy_lint(name = "mypy", deps = None):
    _make_lint_check(name, "mypy", deps or [
        "@pip//mypy",
        "@pip//pydantic", 
        "@pip//pytest",
        "@pip//mypy_boto3_iam",
        "@pip//boto3"
    ])
