from .base import *



ALLOWED_HOSTS = ['*','kaabeporfolio.herokuapp.com']

DEBUG  = True
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS +=[
	# 'cloudinary_storage',
    # 'cloudinary',
    # 'django.contrib.postgres',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
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


#For heroku Specific 
import dj_database_url 
prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)

import django_heroku
django_heroku.settings(locals())