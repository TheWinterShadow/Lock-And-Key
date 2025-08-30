package(default_visibility = ["//visibility:public"])

py_binary(
    name = "isort_check",
    srcs = [],
    main = "@lock_and_key_lib//:isort",
    args = ["--check", "--diff", "lock_and_key/"],
)

py_binary(
    name = "black_check",
    srcs = [],
    main = "@lock_and_key_lib//:black",
    args = ["--check", "lock_and_key/"],
)

py_binary(
    name = "mypy_check",
    srcs = [],
    main = "@lock_and_key_lib//:mypy",
    args = ["lock_and_key/"],
)

genrule(
    name = "build",
    srcs = [],
    outs = ["build.stamp"],
    cmd = "true",
    tools = [
        ":isort_check",
        ":black_check",
        ":mypy_check",
        "//lock_and_key:cli",
    ],
)
