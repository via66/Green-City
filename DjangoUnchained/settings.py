import os
import dj_database_url
"""
Django settings for DjangoUnchained project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eb-sydakr9i06od9271e-53i)hqk)o55x368dz&!bt*q#zh625'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'GreenCity',
    'django_facebook',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'DjangoUnchained.urls'

WSGI_APPLICATION = 'DjangoUnchained.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

PRODUCTION = "PRODUCTION"
DEV = "DEV"
STAGING = "STAGING"

if 'DEPLOYMENT_TYPE' in os.environ:
    DEPLOYMENT = os.environ['DEPLOYMENT_TYPE'].upper()
else:
    DEPLOYMENT = DEV

if DEPLOYMENT == PRODUCTION:
    DEBUG = True
    TEMPLATE_DEBUG = True
    DATABASES = {'default': dj_database_url.config(default=os.environ.get('CLEARDB_DATABASE_URL'))}

    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Allow all host headers
    ALLOWED_HOSTS = ['*']

    # Static asset configuration
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_URL = '/static/'
    STATIC_ROOT = 'staticfiles'

    STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../GreenCity/static'),
        '../static',
    )
    TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  '../templates'),
    )   # for some reason Heroku thinks that this is somewhere else so we have to move directories
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    DEBUG = True
    TEMPLATE_DEBUG = True
    STATIC_URL = '/static/'

    TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
    )
    STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'GreenCity/static'),
        'static',
    )

TEMPLATE_LOADERS = (

    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',

)

#django-facebook changes
FACEBOOK_APP_ID = "296712420453220"
FACEBOOK_APP_SECRET = "2e21f47e04877e61f311d041e3c5c4c4"

TEMPLATE_CONTEXT_PROCESSORS = (
    #default django 1.7 TEMPLATE_CONTEXT_PROCESSORS
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",

    #django-facebook integration
    'django_facebook.context_processors.facebook',
    # and add request if you didn't do so already
    'django.core.context_processors.request',
    )

AUTHENTICATION_BACKENDS = (
    #default django 1.7 AUTHENTICATION_BACKENDS
    'django.contrib.auth.backends.ModelBackend',
    
    #django-facebook integration
    'django_facebook.auth_backends.FacebookBackend',
    )

AUTH_PROFILE_MODULE = 'django_facebook.FacebookProfile'

AUTH_USER_MODEL = 'GreenCity.NewUser'

FACEBOOK_REGISTRATION_TEMPLATE = "GreenCity/register.html"