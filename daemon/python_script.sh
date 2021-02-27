#!/bin/bash

set -e
 
scriptname=$(basename $0)
lock="/var/run/${scriptname}"
echo "test"

 
exec 200>$lock
flock -n 200 || exit 1

echo "pass"

/usr/local/bin/python3.9 /usr/src/app/main.py >> /var/log/cron.log 2>&1

sleep 60
