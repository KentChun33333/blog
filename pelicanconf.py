#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pelican_jupyter import markup as nb_markup



AUTHOR = 'Kent Chiu'
SITENAME = 'Autumn Memo'
SITEURL = 'https://kentchun33333.github.io'
#SITEURL = 'http://localhost:8000' # for test 
SITETITLE = AUTHOR
SITESUBTITLE = 'Algorithm Mind Space'
SITELOGO = 'https://scontent.fsin5-1.fna.fbcdn.net/v/t1.0-1/p720x720/96215235_3403513689663854_7453417891073884160_o.jpg?_nc_cat=106&_nc_sid=dbb9e7&_nc_ohc=FFyXABpAhHQAX9b-fUS&_nc_ht=scontent.fsin5-1.fna&_nc_tp=6&oh=3f722a46a66c21fadc044d92033c0590&oe=5EED0413'
SITEDESCRIPTION = 'Just Memos'
PATH = 'D:/KC-RC'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'


# pelican-THEMES
THEME = "Flex"

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

MARKUP = ("md", "ipynb")

PLUGINS = [nb_markup]

IGNORE_FILES = [".ipynb_checkpoints"]
