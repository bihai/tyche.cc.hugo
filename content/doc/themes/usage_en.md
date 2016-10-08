---
date: 2014-05-12T10:09:27Z
lastmod: 2015-01-27
menu:
  main:
    parent: themes
next: /doc/themes/customizing
prev: /doc/themes/installing
title: Using a Theme
weight: 30
---

Please make certain you have installed the themes you want to use in the
`/themes` directory.

To use a theme for a site:

    hugo -t ThemeName

The *ThemeName* must match the name of the directory inside `/themes`.

Hugo will then apply the theme first, then apply anything that is in the local
directory. To learn more, go to [customizing themes](/doc/themes/customizing/).