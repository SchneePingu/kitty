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

#### Deployment

`Kitty` is configured with `bazel` and `autotools`, that is `autoconf` and `automake`.
To create a release for `kitty`, just execute the command `./bazelisk build Release`.
This will create a `tar.gz` archive ready for distribution in `bazel-bin`.

#### System tests

`Kitty` is tested with Python 3 by means of the `unittest` module.
The tests are located in the `tests` directory and are executed by the bazel commands `./bazelisk test @kitty//tests:SystemTests` and `./bazelisk test @kitty//tests:InstallationTest`
