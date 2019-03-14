#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kent Chiu'
SITENAME = 'Autumn Memo'
SITEURL = 'https://kentchun33333.github.io'
SITETITLE = AUTHOR
SITESUBTITLE = 'Data Scientist'
SITELOGO = SITEURL + '/image/profile.png'
SITEDESCRIPTION = 'Memos from authors, if it is helpful, please consider support me, thank you so ~ much !'
PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'


# pelican-THEMES
THEME = "/Users/kentchiu/Flex"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# DISQUS_SITENAME
# You must regist your site on disqus first
# https://https-kentchun33333-github-io.disqus.com/admin/
DISQUS_SITENAME = 'https-kentchun33333-github-io'

# TOP Menu
MAIN_MENU = True
MENUITEMS = (('Archives', '/archives.html'),
                          ('Categories', '/categories.html'),
                          ('Tags', '/tags.html'),)

# Social widget
SOCIAL = (('linkedin',
           'https://www.linkedin.com/in/kent-chiu-93b745a2?trk=hp-identity-photo'),
          ('github', 'https://github.com/KentChun33333'),
          ('facebook','https://www.facebook.com/kent.chun'),)

# https://github.com/danielfrg/pelican-ipynb/issues/48
IPYNB_IGNORE_CSS = True

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = ['./plugins/']
PLUGINS = ['pelican-ipynb.markup']
