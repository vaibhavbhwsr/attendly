#!/bin/sh

while ! nc -z db 5432; do
    echo "Waiting for postgres..."
    sleep 0.1
done
echo "PostgreSQL started ..."

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/init.json
# python manage.py runserver 0:8000

exec "$@"
