"""
Django settings for corkboard project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from secrets import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(%^u!brr@me%bt+2htvwg%789@e_5iz$2j7eb9)ik8zqdp&@ep'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

ALLOWED_HOSTS = []

LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/cascade/'

EMAIL_HOST = 'mailtrap.io'
EMAIL_HOST_USER = '28756b366a6cfc0ef'
EMAIL_HOST_PASSWORD = '005eba76ee0424'
EMAIL_PORT = '2525'

SITE_ID = 1

BROKER_URL = 'amqp://%s:%s@mapststarcsrv3:5672/celery_vhost' % (RABBITMQ_USER, RABBITMQ_PWD)
# BROKER_URL = 'redis://localhost:6379/0'

CELERY_IMPORTS = ('cascade.tasks',)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'cascade',
    'registration',
    'rest_framework',
    'corsheaders'
)


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request"
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'corkboard.urls'

WSGI_APPLICATION = 'corkboard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Google API
GOOGLE_CLIENT_SECRETS = os.path.join(BASE_DIR, 'corkboard', 'client_secrets.json')
GOOGLE_REDIRECT_URI = 'http://localhost:8008/oauth2callback'

# Registration
ACCOUNT_ACTIVATION_DAYS = 7

# GIS
WKID = 4326
FEATURE_SERVER_URL = 'http://mapststarcsvr1:6080/arcgis/rest/services/SpecialEvents/FeatureServer/0/addFeatures?f=pjson'
GOOGLE_GEOCODE_URL_BASE = 'https://maps.googleapis.com/maps/api/geocode/json?address='

# CORS
CORS_ORIGIN_WHITELIST = (
    'localhost:4200'
)

# DRF
REST_FRAMEWORK = {
    # "DEFAULT_RENDERER_CLASSES": (
    #     "rest_framework_json_api.renderers.JsonApiRenderer",
    #     "rest_framework.renderers.BrowsableAPIRenderer",
    # ),
    # "DEFAULT_PARSER_CLASSES": (
    #     "rest_framework_json_api.parsers.JsonApiParser",
    #     "rest_framework.parsers.FormParser",
    #     "rest_framework.parsers.MultiPartParser",
    # ),
}
