#!/bin/sh

#if [ "$DEBUG" = 1 ]
#then
#    echo "Waiting for database response..."
#
#    while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
#        sleep 0.1
#    done
#
#    echo "Database Started!"
#
#fi
pip uninstall micorservice_demo_with_grpc_shared_utils -y
pip install git+https://github.com/Sir-heed/micorservice-demo-with-grpc-shared-utils.git@main
# python manage.py flush --no-input
python manage.py makemigrations --no-input
python manage.py migrate --no-input
# python manage.py collectstatic --no-input --clear
rm celerybeat.pid

exec "$@"