load('@kitty//:version.bzl', 'VERSION')

filegroup(
    name = "AutotoolsResources",
    srcs = [
        ":AutoconfResources",
        ":AutomakeResources",
    ],
    visibility = ["//visibility:public"],
)

filegroup(
    name = "AutoconfResources",
    srcs = ["configure.ac"],
    visibility = ["//visibility:public"],
)

filegroup(
    name = "AutomakeResources",
    srcs = ["Makefile.am"],
)

genrule(
    name = "GenerateConfigure",
    outs = ["configure.ac"],
    cmd_bash = """
cat << EOF > $@

AC_INIT([kitty], [{version}])
AM_INIT_AUTOMAKE([foreign])

AC_CONFIG_FILES([Makefile])
AC_OUTPUT

EOF
    """.format(version=VERSION),
)

genrule(
    name = "GenerateMakefile",
    srcs = [
        "@kitty//:Documentation",
        "@kitty//man:Manpage",
        "@kitty//sh:Kitty",
        "@kitty//vim:Plugin",
        "@kitty//:Installer"
    ],
    outs = ["Makefile.am"],
    cmd_bash = """
cat << EOF > $@
bin_SCRIPTS = sh/kitty
man1_MANS = $(location @kitty//man:Manpage)

EXTRA_DIST = $(locations @kitty//:Documentation) $(location @kitty//man:Manpage) $(location @kitty//vim:Plugin) $(location @kitty//sh:Kitty) $$(basename $(location @kitty//:Installer))
EOF
    """,
)
