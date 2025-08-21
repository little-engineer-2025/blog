# https://docs.getpelican.com/en/latest/settings.html

SITENAME = 'DevSensation'
# SITEURL = 'https://avisiedo.github.io/blog'

PATH = 'content'
STATIC_PATHS = ['static', 'images', 'favicon.ico']

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
  ('github', 'https://github.com/avisiedo'),
  ('github', 'https://github.com/little-engineer-2025'),
  ('envelope','mailto:learning.little.engineer.2025.1+spam@gmail.com'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# https://github.com/gilsondev/pelican-clean-blog/tree/master?tab=readme-ov-file
THEME = './templates/pelican-clean-blog'

# Template specific
# https://github.com/gilsondev/pelican-clean-blog/tree/master?tab=readme-ov-file#basic-configuration
HEADER_COVER = 'static/header-cover.jpg'
COLOR_SCHEME_CSS = 'monokai.css'
FAVICON = 'favicon.ico'
