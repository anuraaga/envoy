workspace(name = "envoy")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "dlfcn-win32",
    build_file_content = """
cc_library(
    name = "dlfcn-win32",
    srcs = ["src/dlfcn.c"],
    hdrs = ["src/dlfcn.h"],
    includes = ["src"],
    visibility = ["//visibility:public"],
)
""",
    strip_prefix = "dlfcn-win32-1.4.1",
    url = "https://github.com/dlfcn-win32/dlfcn-win32/archive/refs/tags/v1.4.1.tar.gz",
    sha256 = "30a9f72bdf674857899eb7e553df1f0d362c5da2a576ae51f886e1171fbdb399",
)

load("//bazel:api_binding.bzl", "envoy_api_binding")

envoy_api_binding()

load("//bazel:api_repositories.bzl", "envoy_api_dependencies")

envoy_api_dependencies()

load("//bazel:repo.bzl", "envoy_repo")

envoy_repo()

load("//bazel:repositories.bzl", "envoy_dependencies")

envoy_dependencies()

load("//bazel:repositories_extra.bzl", "envoy_dependencies_extra")

envoy_dependencies_extra()

load("//bazel:python_dependencies.bzl", "envoy_python_dependencies")

envoy_python_dependencies()

load("//bazel:dependency_imports.bzl", "envoy_dependency_imports")

envoy_dependency_imports()

load("//bazel:dependency_imports_extra.bzl", "envoy_dependency_imports_extra")

envoy_dependency_imports_extra()
