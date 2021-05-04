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

Kitty is a Linux command line tool to search the current directory - including all non-hidden subdirectories - for files, file contents and directories matching a specific pattern. The result is either displayed on command line or can even be browsed in [Vim](https://www.vim.org/).

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

### VIM(8) plugin

Kitty provides a plugin for VIM 8 to navigate through its output.
This way - when the output of kitty is displayed in VIM - the file or directory,
defined in the line where the cursor is located,
can be opened by `:call KittyGoToSelectedFile()`.
To jump to the next search result, use `:call KittyGoToNextSearchResult()`.
For convenience, the plugin also provides a key mapping for this,
such that files or directories may be opened with `CTRL + l` and closed with `CTRL + h`.
When pressing `CTRL + j`, the cursor jumps to the next search result.
However, this mapping is only applied if not in use already, in order not mess with your setup.
To setup a custom mapping, add the following to `$HOME/.vimrc` and adapt the keys `<c-h>`, `<c-j>` and `<c-l>`:

```bash
map <c-l> :call KittyGoToSelectedFile()<CR>
map <c-h> :q!<CR>
map <silent> <c-j> :silent! call KittyGoToNextSearchResult()<CR>
```

### Kitty developer

#### Deployment

`Kitty` is configured with `bazel` and `autotools`, that is `autoconf` and `automake`.
To create a release for `kitty`, just execute the command `./bazelisk build Release`.
This will create a `tar.gz` archive ready for distribution in `bazel-bin`.

#### System tests

`Kitty` is tested with Python 3 by means of the `unittest` module.
The tests are located in the `tests` directory and are executed by the bazel commands `./bazelisk test @kitty//tests:SystemTests` and `./bazelisk test @kitty//tests:InstallationTest`
