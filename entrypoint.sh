#!/bin/sh

echo "Waiting for DB..."
sleep 5

echo "Running migrations..."
python manage.py migrate --settings=$DJANGO_SETTINGS_MODULE

echo "Collecting static..."
python manage.py collectstatic --noinput --settings=$DJANGO_SETTINGS_MODULE

echo "Starting Server..."
exec "$@"
