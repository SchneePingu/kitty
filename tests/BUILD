py_test(
    name = "SystemTests",
    srcs = ["py/system_tests.py"],
    deps = [":TestHelper"],
    main = "py/system_tests.py",
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
    name = "LintBashCode",
    size = "small",
    srcs = ["LintBashCode.sh"],
    data = ["@kitty//sh:Kitty"],
)

genrule(
    name = "GenerateBashCodeLinter",
    srcs = ["@kitty//sh:Kitty"],
    outs = ["LintBashCode.sh"],
    cmd = """
cat << EOF > $@
shellcheck $(SRCS)
EOF
""",
)

sh_test(
    name = "LintPythonTestCode",
    size = "small",
    srcs = ["LintPythonTestCode.sh"],
    data = [":PythonTestCode"],
)

genrule(
    name = "GeneratePythonTestCodeLinter",
    srcs = [":PythonTestCode"],
    outs = ["LintPythonTestCode.sh"],
    cmd = """
cat << EOF > $@
python3 -m pylint $(SRCS)
EOF
""",
)

filegroup(
    name = "PythonTestCode",
    srcs = glob(["py/*.py"]),
)
