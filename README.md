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

To install `kitty`, download the release archive `kitty-*.tar.gz`, extract it with `tar -xvf kitty-*.tar.gz`, change directory to `kitty-*` and run the following commands:

```bash
./configure
make install
```

Notice, that by default this requires root privileges!
To install `kitty` locally without root privileges use the `--prefix` option to specify an installation directory, for instance:

```bash
./configure --prefix="$HOME/.local"
make install
```

Take care for this directory to be covered by the `PATH` environment variable!

## Vim(8) plugin

Kitty provides a plugin for Vim 8 to navigate through its output.
To install it, we use Vim's native pack system and make `kitty` an optional package.
Assuming that optional packages are located in `~/.vim/pack/plugins/opt`,
this is done by creating the directory `kitty/plugin` and copying the file `explorer.vim` to this new directory.

```bash
mkdir -p ~/.vim/pack/plugins/opt/kitty/plugin
cp ./explorer.vim ~/.vim/pack/plugins/opt/kitty/plugin/explorer.vim
```

This way - when the output of kitty is displayed in Vim - the file or directory,
defined in the line where the cursor is located,
can be opened by `:call KittyExplorePath()`.
For convenience, the plugin also provides a key mapping for this,
such that files or directories may be opened with `CTRL + x` and closed with `CTRL + y`.
However, this mapping is only applied if not in use already, in order not mess with your setup.
To setup a custom mapping, add the following to `~/.vimrc` and adapt the keys `<c-x>` and `<c-y>`:

```bash
map <c-x> :call KittyExplorePath()<CR>
map <c-y> :q!<CR>
```

## Kitty developer

Kitty is configured with `autotools`, that is `autoconf` and `automake`.
To create a release for kitty, just run the bash script `deploy.sh`.

```bash
./deploy.sh
```

This will create a `tar.gz` archive ready for distribution.
