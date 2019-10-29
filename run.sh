#!/bin/bash

cd $(dirname $0)
source ~/.virtualenvs/chapi/bin/activate
SOCKET=$(grep UWSGI_PORT .env | sed 's/.*=\s*//')
exec uwsgi --socket :$SOCKET --ini uwsgi.ini
