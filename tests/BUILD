py_test(
    name = "SystemTests",
    srcs = ["py/SystemTests.py"],
    deps = [":TestHelper"],
)

py_library(
    name = "TestHelper",
    srcs = ["py/TestHelper.py"],
    data = ["data", "@kitty//sh:Kitty"],
)

sh_test(
    name = "InstallationTest",
    size = "small",
    srcs = ["sh/InstallationTest.sh"],
    data = ["@kitty//:Release"],
)
