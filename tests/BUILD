py_test(
    name = "SystemTests",
    srcs = ["py/system_tests.py"],
    deps = [":TestHelper"],
)

py_library(
    name = "TestHelper",
    srcs = ["py/test_helper.py"],
    data = ["data", "@kitty//sh:Kitty"],
)

sh_test(
    name = "InstallationTest",
    size = "small",
    srcs = ["sh/InstallationTest.sh"],
    data = ["@kitty//:Release"],
)

sh_test(
    name = "LinterTest",
    size = "small",
    srcs = ["sh/LinterTest.sh"],
    data = ["@kitty//sh:Kitty"],
)

sh_test(
    name = "PythonLinterTest",
    size = "small",
    srcs = ["PyLinterTest.sh"],
    data = [":PythonTestCode"],
)

genrule(
    name = "GeneratePythonLinterTest",
    srcs = [":PythonTestCode"],
    outs = ["PyLinterTest.sh"],
    cmd = """
cat << EOF > $@
# The 'subprocess' module is ignored,
# because its method 'run' is falsely not recognized as member.
pylint --ignored-modules=subprocess $(SRCS)
EOF
""",
)

filegroup(
    name = "PythonTestCode",
    srcs = glob(["py/*.py"]),
)
