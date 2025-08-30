package(default_visibility = ["//visibility:public"])


genrule(
    name = "isort_check",
    srcs = [
        "//lock_and_key:all_py_files",
    ],
    outs = ["isort_check.out"],
    cmd = "isort --check --diff lock_and_key/ && touch $@",
    tools = ["//lock_and_key:lock_and_key_lib"],
)

genrule(
    name = "black_check",
    srcs = [
        "//lock_and_key:all_py_files",
    ],
    outs = ["black_check.out"],
    cmd = "black --check lock_and_key/ && touch $@",
    tools = ["//lock_and_key:lock_and_key_lib"],
)

genrule(
    name = "mypy_check",
    srcs = [
        "//lock_and_key:all_py_files",
    ],
    outs = ["mypy_check.out"],
    cmd = "mypy lock_and_key/ && touch $@",
    tools = ["//lock_and_key:lock_and_key_lib"],
)
