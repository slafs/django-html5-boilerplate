# Django project settings file
# This file should be part of the project repository of the project and should not
# contains any site-specific information.
# Site-specific information (database name/login/password for example) should be
# in the settings_local.py file and should not be added to the project repository

import os

# By default urllib, urllib2, and the like have no timeout which can cause
# some apache processes to hang until they are forced kill.
# Before python 2.6, the only way to cause them to time out is by setting
# the default timeout on the global socket.

# Uncomment lines below if You need this
#import socket
#socket.setdefaulttimeout(5)

SITE_ID = 1

USE_I18N = True
USE_L10N = True

LANGUAGE_CODE = 'en'

gettext = lambda s: s
LANGUAGES = (('en', gettext('English')),)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'shpaml_loader.filesystem',
    'shpaml_loader.app_directories',
    'shpaml_loader.eggs',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'urls'


PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media/uploaded_media')
STATIC_ROOT = os.path.join(MEDIA_ROOT, 'media/static')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'


STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.

    os.path.join(PROJECT_PATH, 'static/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates/'),
)

FILE_UPLOAD_PERMISSIONS = 0664


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.admin',
    'django.contrib.admindocs',
    
    'testapp',

)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


#########################################################################

# Import settings from local_settings.py, if it exists.
#
# based on this great snippet http://djangosnippets.org/snippets/1873/

try:
  import settings_local
except ImportError:
  print """ 
    -------------------------------------------------------------------------
    You need to create a settings_local.py file which needs to contain at least
    database connection information.
    
    Copy settings_local_example.py to settings_local.py and edit it.
    -------------------------------------------------------------------------
    """
  import sys 
  sys.exit(1)
else:
  # Import any symbols that begin with A-Z. Append to lists any symbols that
  # begin with "EXTRA_".
  import re
  for attr in dir(settings_local):
    match = re.search('^EXTRA_(\w+)', attr)
    if match:
      name = match.group(1)
      value = getattr(settings_local, attr)
      try:
        globals()[name] += value
      except KeyError:
        globals()[name] = value
    elif re.search('^[A-Z]', attr):
      globals()[attr] = getattr(settings_local, attr)

