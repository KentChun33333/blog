#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kent Chiu'
SITENAME = 'Autumn Memo'
SITEURL = 'https://kentchun33333.github.io'
SITETITLE = AUTHOR
SITESUBTITLE = 'Data Scientist'
SITEDESCRIPTION = "Collection of memos from {}".format(AUTHOR)
PATH = 'content'
TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'


# pelican-themes
THEME = "/Users/kentchiu/pelican-themes/Flex"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


MENUITEMS = (('Archives', '/archives.html'),
                          ('Categories', '/categories.html'),
                          ('Tags', '/tags.html'),)

# Social widget
SOCIAL = (('linkedin',
           'https://www.linkedin.com/in/kent-chiu-93b745a2?trk=hp-identity-photo'),
          ('github', 'https://github.com/KentChun33333'),)




DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = ['./plugins']
PLUGINS = ['ipynb.markup']
