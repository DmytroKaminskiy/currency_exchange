#! /bin/bash

python src/manage.py check
flake8 src
python src/manage.py test
pip check
