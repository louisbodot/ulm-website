#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Club Rock 4 Temps ENS Ulm'
SITENAME = 'Club Rock 4 Temps ENS Ulm'

# SITEURL = 'http://ulm.rock4temps.fr/public/output/'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme plugins & extensions

JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n"],
}

# JINJA_EXTENSIONS = JINJA_ENVIRONMENT["extensions"]

PLUGIN_PATHS = ["data/plugins"]
PLUGINS = ["i18n_subsites", "jinja2content", ]
I18N_TEMPLATES_LANG = 'fr'

THEME = "themes/pelican-bootstrap3"
# BOOTSTRAP_THEME = 'simplex'
# BOOTSTRAP_THEME = 'ulm'
BOOTSTRAP_THEME = 'yeti_ulm'

PYGMENTS_STYLE = "monokai"
CUSTOM_CSS = 'theme/css/custom.css'

# Pelican Theme specials

DISPLAY_CATEGORIES_ON_MENU = False
SHOW_ARTICLE_CATEGORY = True
SHOW_ARTICLE_AUTHOR = True
HIDE_SIDEBAR = True

SLUGIFY_SOURCE = 'title'

# Blogroll
LINKS = (
    ('Facebook du P4T', 'https://www.facebook.com/Printemps4Temps/ '),
    ('YouTube du P4T',
     'https://www.youtube.com/channel/UCFU1BM6d0mQzLJkha1idTtw '),
    ("Instagram du P4T", 'https://www.instagram.com/printemps4temps/'),
)

# Social widget
SOCIAL = (
    ('Facebook du Club',
     'https://www.facebook.com/Club-de-rock-4-temps-de-lENS-dUlm-375879339657986/'),
    ('YouTube du Club',
     'https://www.youtube.com/channel/UCENi2WW1tbMwdZFzfaLUu1g'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing

RELATIVE_URLS = False
