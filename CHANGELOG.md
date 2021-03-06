# Changelog
All new features, notable changes and fixes of this project are going to be documented in this file.

## [Unreleased]

### New features

### Notable Changes

### Fixes

## [Kitty 1.5.1]

### New features

### Notable Changes

* Search result is no longer colored.

### Fixes

* Binary files are exluded when searching file content.
* Search result shows only matching lines instead of whole file.

## [Kitty 1.5]

### New features

### Notable Changes

* Test Code is analysed with Pylint linter.
* Kitty is analysed with ShellCheck linter.
* Vim plugin is installed with `make`.
* Installation script was removed.
* Files for autotools are no longer generated by `Bazel`.
* Key mappings of VIM plugin have changed.

### Fixes

* Hidden directories and files are excluded from the search.
* The file for a search result containing a backticks command substitution can be opened with the VIM plugin.

## [Kitty 1.4]

### New features

* Use `install-kitty` script in release archive to install `kitty`.
* Jump to next search result with `:call KittyGoToNextSearchResult()` (`CTRL + SPACE`) in `VIM`.
* Results for file content search are colored when displayed in the command line.
* Search results are displayed in the command line if no `VIM` installation is found.

### Notable Changes

* `Kitty` no longer requires a `sed` installation (Notice, that the `VIM` plugin, however, still does, though).
* A `CHANGELOG` has been introduced.
* `Kitty` is now build and tested with `bazel 4.0.0`.

### Fixes
