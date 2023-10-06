#!/bin/bash
cd /home/ubuntu/ec2-user-django-at-lyskills

source /home/ubuntu/test-django/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt

python3 manage.py migrate
