![kitty](https://img.shields.io/badge/kitty-v1.4-purple.svg)
![license](https://img.shields.io/badge/license-MIT-blue.svg)
![build](https://github.com/SchneePingu/kitty/actions/workflows/deployment.yml/badge.svg)
![tests](https://github.com/SchneePingu/kitty/actions/workflows/tests.yml/badge.svg)
![bash](https://img.shields.io/badge/bash-v4.4-orange.svg)
![bazel](https://img.shields.io/badge/bazel-v4.0-orange.svg)
![python](https://img.shields.io/badge/python-v3.6-orange.svg)
![vim](https://img.shields.io/badge/vim-v8.0-orange.svg)

### What is Kitty?

Kitty is a command line tool (bash script) to search the current directory - including all non-hidden subdirectories - for directories, files and file contents matching a name.

### Kitty usage

Kitty is executed the following way
```bash
kitty [-v] [-c -d -f] NAME
```
where `NAME` specifies the pattern to search for.
To search for directories use the option `-d`, to search for files use the option `-f`, and to search for file contents use the option `-c`. Notice that the options `-d` and `-f` can be used simultaneously, while the option `-c` has a higher precedence.
To display the result in VIM, use the option `-v`.

### Kitty installation

To install `kitty` to `$HOME/.local`, you may use the installer `install-kitty.sh` contained in the release archive.

```bash
curl -L https://www.github.com/yaubik/kitty/releases/download/v1.4/kitty-1.4.tar.gz \
| tar -xz \
&& cd kitty-1.4/ \
&& ./install-kitty.sh \
&& cd .. \
&& rm -rf kitty-1.4
```

### VIM(8) plugin

Kitty provides a plugin for VIM 8 to navigate through its output.
This way - when the output of kitty is displayed in VIM - the file or directory,
defined in the line where the cursor is located,
can be opened by `:call KittyGoToSelectedFile()`.
To jump to the next search result, use `:call KittyGoToNextSearchResult()`.
For convenience, the plugin also provides a key mapping for this,
such that files or directories may be opened with `CTRL + x` and closed with `CTRL + y`.
When pressing `CTRL + SPACE`, the cursor jumps to the next search result.
However, this mapping is only applied if not in use already, in order not mess with your setup.
To setup a custom mapping, add the following to `$HOME/.vimrc` and adapt the keys `<c-x>`, `<c-y>` and `<c-@>`:

```bash
map <c-x> :call KittyGoToSelectedFile()<CR>
map <c-y> :q!<CR>
map <silent> <c-@> :silent! call KittyGoToNextSearchResult()<CR>
```

### Kitty developer

#### Deployment

`Kitty` is configured with `bazel` and `autotools`, that is `autoconf` and `automake`.
To create a release for `kitty`, just execute the command `./bazelisk build @kitty//package:KittyRelease`.
This will create a `tar.gz` archive ready for distribution in `bazel-bin`.

#### System tests

`Kitty` is tested with Python 3 by means of the `unittest` module.
The tests are located in the `tests` directory and are executed by the bazel command `./bazelisk test @kitty//tests:SystemTests`
