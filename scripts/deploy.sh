#!/bin/bash

cd $WORKSPACE

echo "Application will be deployed in 9000 port"

source saswatfinenv/bin/activate
python -m django runserver 0.0.0.0:9000
