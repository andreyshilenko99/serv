"""
Django settings for serv project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a1ri#05%6g6#v-9&lcusxpr2!pi@=)vc^tdr503pa+*lm5d(6t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'leaflet',
    'djgeojson',
    'mappy'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'serv.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'serv.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER': 'test',
        'PASSWORD': '123',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR
STATICFILES_DIRS = [
    'serv/static'
]

# admi = superman pass = 555
LEAFLET_CONFIG = {
    # 'SPATIAL_EXTENT': (5.0, 44.0, 7.5, 46),
    'DEFAULT_CENTER': (59.939095, 30.315868),
    'RESET_VIEW': False,
    'DEFAULT_ZOOM': 10,
    'MIN_ZOOM': 10,
    'MAX_ZOOM': 15,
    'TILES': [('lol', 'http://localhost:8000/static/Tiles/{z}/{x}/{y}.png', {'attribution': '&copy; IGN'})],
    'PLUGINS': {
        'name-of-plugin': {
            'css': ['/static/node_modules/leaflet-draw/dist/leaflet.draw.css',
                    '/static/node_modules/leaflet-draw/dist/leaflet.draw-src.css'],
            'js': ['/static/node_modules/leaflet-draw/dist/leaflet.draw.js',
                   '/static/node_modules/leaflet-draw/dist/leaflet.draw-src.js'],
            'auto-include': True
        },
        'name': {'js': ['/static/node_modules/leaflet-ajax/dist/leaflet.ajax.js'], 'auto-include': True},
        'ggg': {'js': ['/static/node_modules/jquery/dist/jquery.js'], 'auto-include': True}
    }
}
