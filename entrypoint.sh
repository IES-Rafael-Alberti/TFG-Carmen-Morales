#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate
python manage.py makemigrations
python manage.py set_territories
python manage.py get_acumulated --territorio all
python manage.py get_acumulated --territorio pro
python manage.py get_historic

exec "$@"