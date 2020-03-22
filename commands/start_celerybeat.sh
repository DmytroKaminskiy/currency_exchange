#!/bin/bash

rm /srv/project/run/celery.pid
celery -A currency_exchange beat -l info --workdir=/srv/project/src --pidfile=/srv/project/run/celery.pid  --schedule=/srv/project/run/celerybeat-schedule
