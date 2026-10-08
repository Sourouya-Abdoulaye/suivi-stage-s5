#!/bin/bash
# fresh.sh
rm db.sqlite3
uv run manage.py makemigrations stages
uv run manage.py migrate
uv run manage.py migrate stages 0001
uv run manage.py shell < peuplement.py
uv run manage.py createsuperuser
uv run manage.py runserver