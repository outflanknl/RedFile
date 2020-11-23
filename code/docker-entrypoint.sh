#!/bin/bash
#set -e
cd /code/

#sleep 20

while :
do
	echo "Press [CTRL+C] to stop.."
	gunicorn -w 8 --reload --bind 0.0.0.0:8000 wsgi:app
	echo "Exitted, wait 20 seconds for retry"
	sleep 20
done
