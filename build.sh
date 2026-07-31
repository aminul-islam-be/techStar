#!/bin/bash

echo "🚀 Starting build process for techStar..."

# Install dependencies
pip install -r requirements.txt

# Run migrations with fake initial
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Create superuser if not exists (optional)
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin123')" | python manage.py shell

# Collect static files
python manage.py collectstatic --noinput

echo "✅ Build completed!"
