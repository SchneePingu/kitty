filegroup(
    name = "KittyRelease",
    srcs = ["kitty-1.3.tar.gz"]
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
    outs = ["kitty-1.3.tar.gz"],
    cmd_bash = """
    cp $(locations @kitty//autotools:AutotoolsResources) .
    aclocal
    autoconf
    automake --add-missing
    ./configure
    make distcheck
    mv kitty-latest.tar.gz $@
    """,
)

filegroup(
    name = "Documentation",
    srcs = [
        "README.md",
        "LICENSE.md",
    ],
    visibility = ["//visibility:public"]
)
