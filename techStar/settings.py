# ডাটাবেস সেটআপ (PostgreSQL ব্যবহার করবে)
import os
import dj_database_url

# Vercel PostgreSQL ব্যবহার করুন
if os.environ.get('POSTGRES_URL'):
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('POSTGRES_URL'),
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
else:
    # লোকালে SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
