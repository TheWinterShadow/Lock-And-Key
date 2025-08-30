py_library(
    name = "lock_and_key_lib",
    srcs = glob(["*.py"]),
    visibility = ["//visibility:public"],
)

py_binary(
    name = "cli",
    srcs = glob(["*.py"]),
    main = "cli.py",
    deps = [":lock_and_key_lib"],
)
