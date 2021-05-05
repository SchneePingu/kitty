<p align="center"><img src="/imgs/kitty-emblem.svg" alt="kitty" width="250"></p>

<p align="center">
    <a href="https://img.shields.io/badge/kitty-v1.4-purple.svg"><img src="https://img.shields.io/badge/kitty-v1.4-purple.svg" alt="kitty"></a>
    <a href="https://img.shields.io/badge/license-MIT-blue.svg"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="license"></a>
    <a href="https://github.com/SchneePingu/kitty/actions/workflows/deployment.yml/badge.svg"><img src="https://github.com/SchneePingu/kitty/actions/workflows/deployment.yml/badge.svg" alt="build"></a>
    <a href="https://github.com/SchneePingu/kitty/actions/workflows/tests.yml/badge.svg"><img src="https://github.com/SchneePingu/kitty/actions/workflows/tests.yml/badge.svg" alt="test"></a>
    <a href="https://img.shields.io/badge/bash-v4.4-orange.svg"><img src="https://img.shields.io/badge/bash-v4.4-orange.svg" alt="bash"></a>
    <a href="https://img.shields.io/badge/bazel-v4.0-orange.svg"><img src="https://img.shields.io/badge/bazel-v4.0-orange.svg" alt="bazel"></a>
    <a href="https://img.shields.io/badge/python-v3.6-orange.svg"><img src="https://img.shields.io/badge/python-v3.6-orange.svg" alt="python"></a>
    <a href="https://img.shields.io/badge/vim-v8.0-orange.svg"><img src="https://img.shields.io/badge/vim-v8.0-orange.svg" alt="vim"></a>
</p>

### What is Kitty?

Kitty is a Linux command line tool to search the current directory - including all non-hidden subdirectories - for files, file contents and directories matching a specific pattern. The result is either displayed on command line or can even be browsed in [Vim8](https://vim8.org/).

```bash
kitty OPTIONS PATTERN
```

The exact usage of `kitty` is described in detail in its manpage.

```bash
man kitty
```

### Kitty installation

To install `kitty` to the directory `$HOME/.local`,
first download the latest [release](https://github.com/SchneePingu/kitty/releases/latest) tarball and
extract the files.
Then configure the installation and
finally install the files:

```bash
./configure --prefix="$HOME/.local"
make install
```

### Vim plugin

`Kitty` provides a plugin for [Vim8](https://vim8.org/) to easily browse the search result,
that is jump to the next match and open the corresponding files and directories.

The exact usage of the plugin is described in detail in the `kitty` manpage.

```bash
man kitty
```

### Kitty developer

This section is for developers, who want to build a non-released version of `kitty` or even contribute to the project.

The `kitty` development environment relies on a couple of tools to be installed on your system.
* [autoconf](https://www.gnu.org/software/autoconf/autoconf.html)
* [automake](https://www.gnu.org/software/automake/automake.html)
* [make](https://www.gnu.org/software/make/make.html)
* [python3](https://www.python.org/)
* [shellcheck](https://www.shellcheck.net/)
* [pylint](https://pylint.org/)

#### Deployment

`Kitty` is configured with [bazel](https://bazel.build/) and `autotools`, that is [autoconf](https://www.gnu.org/software/autoconf/autoconf.html) and [automake](https://www.gnu.org/software/automake/automake.html).
A tarball - ready for distribution - is created from the top level directory of this project by means of `bazelisk`.

```bash
./bazelisk build Release
```

This creates the tarball `kitty.tar.gz` in the directory `bazel-bin`.

#### System tests

To ensure `kitty` behaves as expected, it is tested with the `unittest` module of Python 3.
These tests are located in the `tests/py` directory and are executed by means of `bazelisk`.

```bash
./bazelisk test @kitty//tests:SystemTests
```

#### Installation test

To ensure `kitty` can be installed properly, the installation process is tested with a shell script.
This test is located in the `tests/sh` directory and is executed by means of `bazelisk`.

```bash
./bazelisk test @kitty//tests:InstallationTest
```

#### Linting

To minimize introducing bugs in the code of `kitty`, the bash code is analyzed with the [ShellCheck](https://www.shellcheck.net/) linter.
The linter is executed by means of `bazelisk`.

```bash
./bazelisk test @kitty//tests:LintBashCode
```

Furthermore, to minimize introducing bugs in the Python test code, it is analyzed with the [Pylint](https://pylint.org/) linter.
The linter is executed by means of `bazelisk`.

```bash
./bazelisk test @kitty//tests:LintPythonTestCode
```
