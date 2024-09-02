"""
Django settings for menu project.
"""

import os


ENV_DIR = os.path.dirname(os.__file__)
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]


SECRET_KEY = 'django-insecure-(#y@^and-)%6qn6t8a^)2fvim!t1!l!f$i7*hjkmiw1&&yr&ql'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'dynamic_raw_id',

    'menu.apps.MenuConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'menu.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'menu.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'menu_db',
        'USER': 'menu_user',
        'PASSWORD': 'menu_pass',
        'HOST': 'db',
        'PORT': '5432',
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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'db.log'),
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        # 'django.db.backends': {
        #     'handlers': ['file', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': False,
        # },
    },
}


LANGUAGE_CODE = 'ru'
#LANGUAGE_CODE = 'en'

USE_I18N = True
USE_L10N = True
USE_TZ = True

TIME_ZONE = 'Europe/Moscow'

LOCALES = {
    'ru': 'ru_RU.UTF-8',
    'en': 'en_US.UTF-8',
}

LANGUAGES = (
    ('ru', 'ru'),
    ('en', 'en'),
)


STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
