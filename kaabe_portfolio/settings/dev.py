from .base import *

DEBUG  = True
DEBUG404 = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS +=[
	# 'debug_toolbar',
]


MIDDLEWARE += [
	# "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# INTERNAL_IPS = ('127.0.0.1',)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': (BASE_DIR/'db.sqlite3'),
    }
}


# Static files (CSS, JavaScript, Images)
STATIC_ROOT = (BASE_DIR / 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    (BASE_DIR / 'static'),
)


MEDIA_URL = '/media/'
MEDIA_ROOT = (BASE_DIR / 'media/')

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'