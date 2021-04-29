load('@kitty//:version.bzl', 'VERSION')

filegroup(
    name = "KittyRelease",
    srcs = ["kitty-{}.tar.gz".format(VERSION)]
)

genrule(
    name = "MakeKitty",
    srcs = [
        "@kitty//sh:Kitty",
        "@kitty//package/autotools:AutotoolsResources",
        "@kitty//:Documentation",
        "@kitty//man:Manpage",
        "@kitty//vim:Plugin",
        "@kitty//:Installer"
    ],
    outs = ["kitty-{}.tar.gz".format(VERSION)],
    cmd_bash = """
cp $(location @kitty//:Installer) .
cp $(locations @kitty//package/autotools:AutotoolsResources) .
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
        "CHANGELOG.md",
    ],
    visibility = ["//visibility:public"]
)

filegroup(
    name = "Installer",
    srcs = [":InstallKitty"],
    visibility = ["//visibility:public"],
)

genrule(
    name = "InstallKitty",
    srcs = [
        "@kitty//vim:Plugin",
    ],
    outs = ["install-kitty.sh"],
    # Using the construct '$$(echo $$)HOME' is a hack to write '$HOME' without interpreting it as a shell variable
    cmd_bash = """
cat << EOF > $@
./configure --prefix="$$(echo $$)HOME/.local"
make install
mkdir -p "$$(echo $$)HOME/.vim/pack/plugins/opt/kitty/plugin"
cp $(location @kitty//vim:Plugin) "$$(echo $$)HOME/.vim/pack/plugins/opt/kitty/plugin/$$(basename $(location @kitty//vim:Plugin))"
EOF
""",
)

