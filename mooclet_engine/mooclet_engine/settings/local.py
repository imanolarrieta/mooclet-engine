import os
# set default environment variable before importing base settings
# os.environ.setdefault('ENV_TYPE', 'local')

from .base import *
from .secure import *

DEBUG = True

ALLOWED_HOSTS = []

# INSTALLED_APPS += ('debug_toolbar', 'sslserver')

# MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# For Django Debug Toolbar:
INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)

# DEBUG_TOOLBAR_CONFIG = {
#    'INTERCEPT_REDIRECTS': False,
# }


# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATIC_URL = '/static/'
# STATIC_ROOT = normpath(join(SITE_ROOT, 'http_static'))
