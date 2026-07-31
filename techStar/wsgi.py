"""
WSGI config for techStar project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techStar.settings')

application = get_wsgi_application()
