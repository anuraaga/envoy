load("@rules_foreign_cc//foreign_cc:configure.bzl", "configure_make")
load("//bazel:envoy_build_system.bzl", "envoy_package")

licenses(["notice"])  # Apache 2

envoy_package()

exports_files(["dlfcn_win32.BUILD"])

configure_make(
    name = "dlfcn_win32",
    configure_in_place = True,
    configure_options = [
        "--disable-shared",
        "--enable-static",
    ],
    lib_source = "@com_github_dlfcn_win32//:all",
    out_static_libs = ["libdl.a"],
    target_compatible_with = ["@platforms//os:windows"],
)
