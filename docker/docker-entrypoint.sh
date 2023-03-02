#!/bin/bash
python manage.py makemigrations
python manage.py migrate     # Apply database migrations 
   python manage.py collectstatic --noinput
/usr/local/bin/supervisord
