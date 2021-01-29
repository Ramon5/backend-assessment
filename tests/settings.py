import os
from application.settings import INSTALLED_APPS, ROOT_URLCONF, BASE_DIR, Path
from django.core.management.utils import get_random_secret_key

SECRET_KEY = get_random_secret_key()
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'settings/testdb.sqlite3'),
    }
}