#!/bin/bash
# fresh.sh
rm db.sqlite3
uv run manage.py makemigrations stages
uv run manage.py migrate
uv run manage.py migrate stages 0001
uv run manage.py loaddata data.json
uv run manage.py createsuperuser
uv run manage.py runserver