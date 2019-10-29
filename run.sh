#!/bin/bash

cd $(dirname $0)
SOCKET=$(grep UWSGI_PORT .env | grep -oP '\"\K.*(?=")')
VIRTUALENV_PATH=$(grep VIRTUALENV_PATH .env | grep -oP '\"\K.*(?=")')
source $VIRTUALENV_PATH/bin/activate
exec uwsgi --socket :$SOCKET --ini uwsgi.ini
