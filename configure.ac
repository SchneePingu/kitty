AC_INIT([kitty], [1.2])
AM_INIT_AUTOMAKE([foreign])

AC_PATH_PROG([GREP], [grep], [nogrep])
if test "$GREP" = nogrep
then
   AC_MSG_ERROR(['Grep' installation cannot be found])
fi

AC_PATH_PROG([SED], [sed], [nosed])
if test "$SED" = nosed
then
   AC_MSG_ERROR(['sed' installation cannot be found])
fi

AC_PATH_PROG([VIM], [vim], [novim])
if test "$VIM" = novim
then
   AC_MSG_ERROR(['vim' installation cannot be found])
fi

AC_CONFIG_FILES([Makefile])
AC_CONFIG_FILES([kitty], [chmod +x kitty])
AC_CONFIG_FILES([kitty.man])
AC_OUTPUT
