"""
WSGI config for knuwebsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'knuwebsite.settings')

application = get_wsgi_application()
# deploy할 때, static file들을 관리하기 위한 설정
application = DjangoWhiteNoise(application)