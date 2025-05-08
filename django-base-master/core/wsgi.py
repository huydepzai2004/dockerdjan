"""
WSGI config for core project.

This file exposes the WSGI callable as a module-level variable named ``application``.

For more information, see:
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Default to 'core.settings' unless DJANGO_SETTINGS_MODULE is set externally
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()