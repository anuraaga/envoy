load("@rules_foreign_cc//foreign_cc:configure.bzl", "configure_make")
load("//bazel:envoy_build_system.bzl", "envoy_package")

licenses(["notice"])  # Apache 2

envoy_package()

exports_files([
    "cel-cpp.patch",
    "dlfcn_win32.BUILD",
    "luajit.patch",
    "proto-converter.patch",
])

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

# The registry's native LuaJIT build currently supports only Linux and macOS.
configure_make(
    name = "luajit",
    configure_command = "luajit_build_win.sh",
    env = select({
        "//bazel:windows_dbg_build": {"WINDOWS_DBG_BUILD": "debug"},
        "//conditions:default": {},
    }),
    lib_source = "@luajit//:all",
    out_include_dir = "include/luajit-2.1",
    out_static_libs = ["lua51.lib"],
    target_compatible_with = ["@platforms//os:windows"],
    targets = [],
)
