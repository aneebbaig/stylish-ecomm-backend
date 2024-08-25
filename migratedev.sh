#!/bin/bash
export DJANGO_SETTINGS_MODULE='stylish.settings.development'
export $(grep -v '^#' .env.dev | xargs)
python manage.py makemigrations
python manage.py migrate
