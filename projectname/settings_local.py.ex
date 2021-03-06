# Django project site specific settings
# All non site specific settings should go into the settings.py file
# Copy this file as settings_local.py and adjust it to your site.
# The settings_local.py contains only site specific information and should not
# be part of the svn repository of the project. It should be part of the
# hosting svn repository.

DEBUG = True #TODO set to off for live, staging and preview
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = '(xxq$%nk3o!4q_)xfwb88u3=^mki2k7&-i&qq=l@1h_6(6)-0i' #TODO Change on production

#TODO: replace localhost with the domain name of the site
DEFAULT_FROM_EMAIL = 'messenger@localhost'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                             # Or path to database file if using sqlite3.
        'USER': '',                             # Not used with sqlite3.
        'PASSWORD': '',                         # Not used with sqlite3.
        'HOST': '',                             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                             # Set to empty string for default. Not used with sqlite3.
    }
}

INTERNAL_IPS = ('127.0.0.1', )

# TODO: MEDIA_URL needs to be a full URL on production
# in case some media (images) are embedded in another site

#MEDIA_URL = '/media/' #TODO: on production (full URL to the media server)
#STATIC_URL = '/static/'
#ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# Add Django Debug Toolbar application. (It's cool.)
EXTRA_MIDDLEWARE_CLASSES = ( 
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

EXTRA_INSTALLED_APPS = ( 
    'debug_toolbar',
)

