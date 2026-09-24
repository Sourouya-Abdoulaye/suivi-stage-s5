#!/bin/bash
# fresh.sh
rm db.sqlite3
uv run manage.py migrate
uv run manage.py loaddata data.json
uv run manage.py createsuperuser
uv run manage.py runserver