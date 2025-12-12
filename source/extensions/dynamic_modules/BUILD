load(
    "//bazel:envoy_build_system.bzl",
    "envoy_cc_library",
    "envoy_extension_package",
)

licenses(["notice"])  # Apache 2

envoy_extension_package()

envoy_cc_library(
    name = "dynamic_modules_lib",
    srcs = ["dynamic_modules.cc"],
    hdrs = [
        "abi.h",
        "dynamic_modules.h",
    ],
    deps = [
        ":abi_version_lib",
        "//envoy/common:exception_lib",
    ] + select({
        "//bazel:windows_x86_64": ["@dlfcn-win32//:dlfcn-win32"],
        "//conditions:default": [],
    }),
)

envoy_cc_library(
    name = "abi_version_lib",
    hdrs = [
        "abi_version.h",
    ],
)

genrule(
    name = "dynamic_modules_exports",
    srcs = ["abi.h"],
    outs = ["dynamic_modules_exports.def"],
    cmd = "$(location //tools:gen_dynamic_modules_def) $(location abi.h) $@",
    tools = ["//tools:gen_dynamic_modules_def"],
    visibility = ["//visibility:public"],
)
