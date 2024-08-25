from .base import *

DEBUG=True
SECRET_KEY='django-insecure--rxlx18zxu&kzj0dkrv0*d)0mz8_p1@eu3bb%o)(0-q)_qk&r8'


DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'stylish_db',
    'USER': 'aneeb',
    'PASSWORD': 'Hibaneeb@1406',
    'HOST': 'localhost',
    'PORT': 5432,
    'OPTIONS': {
      'sslmode': 'require',
    },
  }
}

