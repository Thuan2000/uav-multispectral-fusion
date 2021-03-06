"""
Django settings for example_labeller_app project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from image_labelling_tool import labelling_tool

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3+p2$qln6o1ws1c)6o!+o+p%ql1n!+tt@wp)g5!pfgliqld)yo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'image_labelling_tool',
    'example_labeller',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'example_labeller_app.urls'

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
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'example_labeller_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '..', 'ext_static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CSRF_COOKIE_SECURE = False



# Labelling tool configuration, used in `example_labeller.views`

# Label classes
# Tuple entries arameters are: symbolic name, human readable name for UI, and colours by colour scheme.
# The user can choose between colour schemes, this is useful when there are lots of label classes,
# making it difficult to choose a range of colours that are easily differentiable from one another.
# They given human readable names that are displayed in the UI in the `tools.colour_schemes` section of the
# `LABELLING_TOOL_CONFIG` dictionary below.
LABEL_CLASSES = [
    labelling_tool.LabelClassGroup('Natural', [
        labelling_tool.LabelClass('tree', 'Trees', dict(default=[0, 255, 192], natural=[0, 255, 192],
                                                        artificial=[128, 128, 128])),
        labelling_tool.LabelClass('lake', 'Lake', dict(default=[0, 128, 255], natural=[0, 128, 255],
                                                       artificial=[128, 128, 128])),
    ]),
    labelling_tool.LabelClassGroup('Artificial', [
        labelling_tool.LabelClass('building', 'Buldings', dict(default=[255, 128, 0], natural=[128, 128, 128],
                                                               artificial=[255, 128, 0])),
    ])]


# Configuration
LABELLING_TOOL_CONFIG = {
    'tools': {
        'imageSelector': True,
        'labelClassSelector': True,
        'brushSelect': True,
        'labelClassFilter': True,
        'drawPointLabel': True,
        'drawBoxLabel': True,
        'drawPolyLabel': True,
        'compositeLabel': True,
        'groupLabel': True,
        'deleteLabel': True,
        'colour_schemes': [dict(name='default', human_name='All'),
                           dict(name='natural', human_name='Natural'),
                           dict(name='artificial', human_name='Artifical')],
        'deleteConfig': {
            'typePermissions': {
                'point': True,
                'box': True,
                'polygon': True,
                'composite': True,
                'group': True,
            }
        }
    }
}
