#!/bin/bash

rm /srv/project/run/celery.pid
celery -A currency_exchange worker -l info --workdir=/srv/project/src --pidfile=/srv/project/run/celery.pid
