# Changelog
All new features, notable changes and fixes of this project are going to be documented in this file.

## [Unreleased]

### New features

* Jump to next search result with `:call KittyGoToNextSearchResult()` (`CTRL + SPACE`) in `VIM`.
* Results for file content search are colored when displayed in the command line.
* Search results are displayed in the command line if no `VIM` installation is found.

### Notable Changes

* `Kitty` no longer requires a `sed` installation (Notice, that the `VIM` plugin, however, still does, though).
* A `CHANGELOG` has been introduced.
* `Kitty` is now build and tested with `bazel 4.0.0`.

### Fixes
