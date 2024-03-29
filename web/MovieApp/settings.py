"""
Django settings for MovieApp project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(" ")
SECRET_KEY = config('SECRET_KEY')
# Application definition

SUPER_USER_NAME=config('SUPER_USER_NAME')
SUPER_USER_PASS=config('SUPER_USER_PASS')

INSTALLED_APPS = [
    'rest_framework' ,
    'moviesite' ,
    'django.contrib.admin' ,
    'django.contrib.auth' ,
    'django.contrib.contenttypes' ,
    'django.contrib.sessions' ,
    'django.contrib.messages' ,
    'django.contrib.staticfiles' ,
    'storages' ,
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware' ,
    'django.contrib.sessions.middleware.SessionMiddleware' ,
    'django.middleware.common.CommonMiddleware' ,
    'django.middleware.csrf.CsrfViewMiddleware' ,
    'django.contrib.auth.middleware.AuthenticationMiddleware' ,
    'django.contrib.messages.middleware.MessageMiddleware' ,
    'django.middleware.clickjacking.XFrameOptionsMiddleware' ,
]

ROOT_URLCONF = 'MovieApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates' ,
        'DIRS': [BASE_DIR / 'moviesite/templates'] ,
        'APP_DIRS': True ,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug' ,
                'django.template.context_processors.request' ,
                'django.contrib.auth.context_processors.auth' ,
                'django.contrib.messages.context_processors.messages' ,
            ] ,
        } ,
    } ,
]

WSGI_APPLICATION = 'MovieApp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
if DEBUG:
    DATABASES = {
        'default': {
            'HOST': config('DATABASE_HOST'),
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': config('DATABASE_USER'),
            'PASSWORD': config('DATABASE_PASS'),
            'NAME': config('DATABASE_NAME'),
            'PORT': config('DATABASE_PORT')
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

if DEBUG:
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID_BUCKET')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY_BUCKET')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = None
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # s3 static settings
    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE = 'MovieApp.storage_backends.StaticStorage'
    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'MovieApp.storage_backends.PublicMediaStorage'
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, "static")


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator' ,
    } ,
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator' ,
    } ,
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator' ,
    } ,
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator' ,
    } ,
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
