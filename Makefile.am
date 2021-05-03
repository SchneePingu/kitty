bin_SCRIPTS = sh/kitty
man1_MANS = man/kitty.man

EXTRA_DIST = man/kitty.man vim/explorer.vim sh/kitty README.md LICENSE.md CHANGELOG.md

install-data-hook:
	mkdir -p "${HOME}/.vim/pack/plugins/opt/kitty/plugin"
	cp $(srcdir)/vim/explorer.vim "${HOME}/.vim/pack/plugins/opt/kitty/plugin/explorer.vim"
