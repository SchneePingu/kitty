def Release():
    native.filegroup(
        name = "Release",
        srcs = ["kitty.tar.gz"],
        visibility = ["//visibility:public"],
    )

    native.genrule(
        name = "GenerateRelease",
        srcs = [
            "@kitty//sh:Kitty",
            "@kitty//:Documentation",
            "@kitty//man:Manpage",
            "@kitty//vim:Plugin",
            "@kitty//:Autotools"
        ],
        outs = ["kitty.tar.gz"],
        cmd_bash = """
aclocal
autoconf
automake --add-missing
./configure
make distcheck
mv kitty-*.tar.gz $@
""",
)

