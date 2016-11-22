#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kent Chiu'
SITENAME = u'Autumn Memo'
SITEURL = 'https://kentchun33333.github.io'
SITESUBTITLE = 'Data Scientist'
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


LINKS = (('Categories', 'https://kentchun33333.github.io/categories.html'),
         ('Tags', 'https://kentchun33333.github.io/tags.html'),
         ('Archives', 'https://kentchun33333.github.io/archives.html'))

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
