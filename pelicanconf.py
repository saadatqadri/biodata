#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Saadat Qadri'
SITENAME = u'Saadat Qadri'
SITEURL = "http://saadatqadri.com"

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DISPLAY_PAGES_ON_MENU = False
DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR=True
BOOTSTRAP_THEME = 'readable'

# Blogroll
LINKS =  (('DatesByTryst', 'http://gettryst.com/'),
          ('Writings on Medium', 'https://medium.com/@saadatqadri'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/saadatqadri'),
          ('GitHub', 'http://github.com/saadatqadri'),
          ('LinkedIn', 'http://linkedin.com/en/saadatqadri'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/home/saadat/code/biodata/pelican-bootstrap3"
