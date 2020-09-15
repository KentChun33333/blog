#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pelican_jupyter import markup as nb_markup



AUTHOR = 'Kent Chiu'
SITENAME = 'Autumn Memo'
SITEURL = 'https://kentchun33333.github.io'
#SITEURL = 'http://localhost:8000' # for test 
SITETITLE = AUTHOR
SITESUBTITLE = 'Mind Space'
SITELOGO = 'https://media-exp1.licdn.com/dms/image/C5103AQGzhSVAx7ReaA/profile-displayphoto-shrink_400_400/0?e=1605744000&v=beta&t=tXvm7MTbUp1JcLLnMymOVBiHLfs0mDiRNQGn7zzryrc'
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
