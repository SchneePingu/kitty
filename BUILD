load('@kitty//:release.bzl', 'Release')

filegroup(
    name = "Documentation",
    srcs = [
        "README.md",
        "LICENSE.md",
        "CHANGELOG.md",
    ],
    visibility = ["//visibility:public"]
)

filegroup(
    name = "Autotools",
    srcs = [
        "configure.ac",
        "Makefile.am",
    ],
    visibility = ["//visibility:public"]
)

Release()
