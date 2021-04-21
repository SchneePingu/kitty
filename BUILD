load('@kitty//:version.bzl', 'VERSION')

filegroup(
    name = "KittyRelease",
    srcs = ["kitty-{}.tar.gz".format(VERSION)]
)

genrule(
    name = "MakeKitty",
    srcs = [
        "@kitty//sh:Kitty",
        "@kitty//autotools:AutotoolsResources",
        "@kitty//:Documentation",
        "@kitty//man:Manpage",
        "@kitty//vim:Plugin",
    ],
    outs = ["kitty-{}.tar.gz".format(VERSION)],
    cmd_bash = """
    cp $(locations @kitty//autotools:AutotoolsResources) .
    aclocal
    autoconf
    automake --add-missing
    ./configure
    make distcheck
    mv kitty-{version}.tar.gz $@
    """.format(version=VERSION),
)

filegroup(
    name = "Documentation",
    srcs = [
        "README.md",
        "LICENSE.md",
    ],
    visibility = ["//visibility:public"]
)
