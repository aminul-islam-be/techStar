#!/bin/bash

echo "🚀 Starting build process for techStar..."

pip install -r requirements.txt
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput

echo "✅ Build completed!"
