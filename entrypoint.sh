#!/bin/bash

# Only collect static files if explicitly requested
if [ "$COLLECT_STATIC" = "true" ]; then
    echo "Collecting static files..."
    python manage.py collectstatic --noinput
else
    echo "Skipping static files collection..."
fi

# Start gunicorn
exec gunicorn mysite.wsgi:application --bind 0.0.0.0:8000