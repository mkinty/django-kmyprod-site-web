import os

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kmyprodsite',
        'USER': 'moustaphak',
        'PASSWORD': 'mkinty',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}


