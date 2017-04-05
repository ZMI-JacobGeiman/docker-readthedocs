from readthedocs.settings.dev import *

import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME', 'db'),
        'USER': os.getenv('DB_USER', 'root'),
        'PASSWORD': os.getenv('DB_PASS', 'root'),
        'HOST': os.getenv('DB_HOST', 'db'),
        'PORT': os.getenv('DB_PORT_NUM', '5432'),
    }
}
SITE_ROOT = '/app'
ES_HOSTS = [os.getenv('ES_HOST', 'elasticsearch:9200')]
REDIS = {
    'host': os.getenv('REDIS_HOST', 'redis'),
    'port': os.getenv('REDIS_PORT_NUM', '6379'),
    'db': os.getenv('REDIS_DB_NUM', '0'),
}
BROKER_URL = 'redis://{}:{}/{}'.format(os.getenv('REDIS_HOST', 'redis'), os.getenv('REDIS_PORT_NUM', '6379'), os.getenv('REDIS_DB_NUM', '0'))
CELERY_RESULT_BACKEND = 'redis://{}:{}/{}'.format(os.getenv('REDIS_HOST', 'redis'), os.getenv('REDIS_PORT_NUM', '6379'), os.getenv('REDIS_DB_NUM', '0'))
DEBUG = True
CELERY_ALWAYS_EAGER = False
ALLOW_PRIVATE_REPOS = True

