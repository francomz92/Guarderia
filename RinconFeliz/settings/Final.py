from .Base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgreslq',
		'HOST': 'db_host',
		'PORT': 'db_port',
        'NAME': 'db_name',
		'USER': 'db_username',
		'PASSWORD': 'db_password'
    }
}
