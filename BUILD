filegroup(
    name = "KittyRelease",
    srcs = ["kitty-1.3.tar.gz"]
)

genrule(
    name = "MakeKitty",
    srcs = [
        "@kitty//sh:Kitty",
        "@kitty//:AutotoolsResources",
        "@kitty//:Documentation",
        "@kitty//:VimPlugin",
    ],
    outs = ["kitty-1.3.tar.gz"],
    cmd_bash = """
    aclocal
    autoconf
    automake --add-missing
    ./configure
    make distcheck
    mv kitty-latest.tar.gz $@
    """,
)

filegroup(
    name = "AutotoolsResources",
    srcs = [
        "configure.ac",
        "Makefile.am"
    ],
)

filegroup(
    name = "Documentation",
    srcs = [
        "README.md",
        "LICENSE.md",
        "kitty.man",
    ],
)

filegroup(
    name = "VimPlugin",
    srcs = ["explorer.vim"],
)
