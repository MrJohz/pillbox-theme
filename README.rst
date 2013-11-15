The Pillbox Theme
=================


Configuration Variables
-----------------------

``PILLBOX_THEMES``
A list of the available colour schemes.  Optional.  Defaults to the include 'dark' and 'light' themes.

``PILLBOX_THEME_DEFAULT``
Of the list ``PILLBOX_THEMES``, the one which should be used as the default.  Optional.  Can only be set f ``PILLBOX_THEMES`` is defined, in which case it defaults to the first item in ``PILLBOX_THEMES``.

``NO_THEME_SWITCHER``
If set to a truthy value, will ensure that the theme switcher is not enabled.  The default theme will be dark.

``QUOTES``
A list of quotes.  These will be included in the index html file, and a random one will be chosen by javascript magic each time the page is loaded.  If this is not defined, no quotes will show.


TODO:
-----

- Add screenshots
- Deal with line-numbers and code
- Ensure every page works
- Add search compatibility
- Document custom themes / inv builds