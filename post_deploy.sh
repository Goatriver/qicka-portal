#!/usr/bin/env bash

chmod 775 ./ -R

if [ ! -d "venv" ]; then
  echo "Creating virtual environment"
  python3.7 -m venv venv
fi

PYTHON="venv/bin/python3"
PIP="venv/bin/pip3"

# install dependencies

$PIP install -r requirements.txt

# manage.py commands
$PYTHON manage.py collectstatic --noinput
$PYTHON manage.py migrate