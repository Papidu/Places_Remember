"""
Django settings for Places_Remember project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from ctypes import CDLL
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

if os.name == 'nt':
    import platform

    OSGEO4W = r"C:\OSGeo4W"
    if '64' in platform.architecture()[0]:
        OSGEO4W += "64"
    assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W
    os.environ['OSGEO4W_ROOT'] = OSGEO4W
    os.environ['GDAL_DATA'] = OSGEO4W + r"\share\gdal"
    os.environ['PROJ_LIB'] = OSGEO4W + r"\share\proj"
    os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH']

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p^buy@a3_rj#g#*njg*hj1zaws@xs6td6wdu_du$4^$fh6egy3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['floating-sea-39932.herokuapp.com', 'localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    'rest_framework',
    'rest_framework_gis',
    'social_django',
    'leaflet',

    'remembers',
]
# GDAL_LIBRARY_PATH = r'C:\OSGeo4W64\bin\gdal202'


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

ROOT_URLCONF = 'Places_Remember.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Places_Remember.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# 'ENGINE': 'django.contrib.gis.db.backends.postgis', 'django.db.backends.postgresql_psycopg2',
import dj_database_url


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'remembers_db',
        'USER': 'postgres',
        'PASSWORD': '1',
        'HOST': 'localhost',
        'PORT': '',
    }
}

import dj_database_url

prod_db = dj_database_url.config(default="postgis://asrpxjficvfxbk:bba041de4abb7cf500fdc18f7030d8bff0c2973325861981c4af01172efc5469@ec2-52-205-61-60.compute-1.amazonaws.com:5432/df70mrje4dvl1o")
DATABASES['default'].update(prod_db)
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
print(DATABASES['default'])
print("------------------------------------")
GDAL_LIBRARY_PATH = os.environ.get('GDAL_LIBRARY_PATH')
GEOS_LIBRARY_PATH = os.environ.get('GEOS_LIBRARY_PATH')

# if os.getenv('DYNO'):
#     GDAL_LIBRARY_PATH = os.path.expandvars(os.getenv('GDAL_LIBRARY_PATH'))
#     GEOS_LIBRARY_PATH = os.path.expandvars(os.getenv('GEOS_LIBRARY_PATH'))
#     DATABASES['default'] =  dj_database_url.parse(os.getenv('DATABASE_URL'),'django.contrib.gis.db.backends.postgis')
#     print(DATABASES['default'])


AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATIC_ROOT = os.path.join(BASE_DIR, "live-static", "static-root")

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#STATIC_ROOT = "/home/cfedeploy/webapps/cfehome_static_root/"

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "live-static", "media-root")

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}

SOCIAL_AUTH_FACEBOOK_KEY = '222867219308894'
SOCIAL_AUTH_FACEBOOK_SECRET = '25f40fcf0f3ed3dddd05d06f6892923b'

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (37.6171875, 55.78275147606406),
    'DEFAULT_ZOOM': 10,
    'MAX_ZOOM': 30,
    'MIN_ZOOM': 5,
    'SCALE': 'both',
}
import django_heroku
django_heroku.settings(locals())