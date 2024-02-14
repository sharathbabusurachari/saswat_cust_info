#!/bin/bash

cd $WORKSPACE

echo "Application will be deployed in 9000 port"

source saswatfinenv/bin/activate
nohup python3 manage.py runserver qa05ci01.com:9000 &
sleep 60
