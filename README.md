## What is Kitty?

Kitty is a command line tool (bash script) to search the current directory - including all non-hidden subdirectories - for directories, files and file contents matching a name.

## Kitty usage

Kitty is executed the following way
```bash
kitty [-c -d -f] NAME
```
where `NAME` specifies the pattern to search for.
To search for directories use the option `-d`, to search for files use the option `-f`, and to search for file contents use the option `-c`. Notice that the options `-d` and `-f` can be used simultaneously, while the option `-c` has a higher precedence.

## Kitty installation

To install `kitty` to `$HOME/.local`, you may use the following command:

```bash
curl -L https://www.github.com/yaubik/kitty/releases/download/v1.2/kitty-1.2.tar.gz \
| tar -xz \
&& cd kitty-1.2/ \
&& ./configure --prefix="$HOME/.local" \
&& make install \
&& mkdir -p $HOME/.vim/pack/plugins/opt/kitty/plugin \
&& cp explorer.vim $HOME/.vim/pack/plugins/opt/kitty/plugin/explorer.vim \
&& cd .. \
&& rm -rf kitty-1.2
```

If you want to install `kitty` to a directory other than `$HOME/.local`, please adapt the path specified by the `--prefix` option.
Take care for this path to be covered by the `PATH` environment variable!

## Vim(8) plugin

Kitty provides a plugin for Vim 8 to navigate through its output.
This way - when the output of kitty is displayed in Vim - the file or directory,
defined in the line where the cursor is located,
can be opened by `:call KittyExplorePath()`.
For convenience, the plugin also provides a key mapping for this,
such that files or directories may be opened with `CTRL + x` and closed with `CTRL + y`.
However, this mapping is only applied if not in use already, in order not mess with your setup.
To setup a custom mapping, add the following to `$HOME/.vimrc` and adapt the keys `<c-x>` and `<c-y>`:

```bash
map <c-x> :call KittyExplorePath()<CR>
map <c-y> :q!<CR>
```

## Kitty developer

`Kitty` is configured with `autotools`, that is `autoconf` and `automake`.
To create a release for `kitty`, just execute the bash script `deploy.sh`.
This will create a `tar.gz` archive ready for distribution.
