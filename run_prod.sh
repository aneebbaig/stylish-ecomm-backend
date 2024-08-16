#!/bin/bash
export DJANGO_SETTINGS_MODULE='stylish.settings.production'
export $(grep -v '^#' .env.prod | xargs)
gunicorn your_project.wsgi:application
