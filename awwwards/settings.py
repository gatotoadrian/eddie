
import os
from pathlib import Path


import cloudinary
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^4(s086u*b#h%-u564xmqd(x**t20$yy3-x(%^5n&9p(kf&h+n'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = ['.localhost', '.127.0.0.1',
                 '.0.0.0.0', '.awwwards-xxiv.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    "whitenoise.runserver_nostatic",
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'members.apps.MembersConfig',
    'home.apps.HomeConfig',
    'rest_framework'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'awwwards.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'awwwards.wsgi.application'


# Database
# DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
# #         'NAME': 'Awwwards',
# #         'USER': 'kiama',
# #         'PASSWORD': 'kiamapwd',
# #         'HOST': 'localhost',
# #     }
# # }

# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# postgres://cbvfupibjxrrvt:ba6626a05c974ea3802419320eeeec245f72f86cb2b09f3d4ee518687ab09563@ec2-44-194-4-127.compute-1.amazonaws.com:5432/de8mnrpjb6qjrb

#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'de8mnrpjb6qjrb',
        'USER': 'cbvfupibjxrrvt',
        'PASSWORD': 'ba6626a05c974ea3802419320eeeec245f72f86cb2b09f3d4ee518687ab09563',
        'HOST': 'ec2-44-194-4-127.compute-1.amazonaws.com',
        'PORT': 5432
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [

]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'


ROOT_PATH = os.path.dirname(__file__)


STATICFILES_DIRS = [os.path.join(ROOT_PATH, 'static')]
FILE_CHARSET = 'utf-8'


LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


cloudinary.config(
    cloud_name="dvua6fhuc",
    api_key="242318296529564",
    api_secret="0l6qjwjrmEFXuT__sbCZgLm1Xyc"
)


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
