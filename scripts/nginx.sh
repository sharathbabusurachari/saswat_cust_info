#!/bin/bash

sudo cp -rf app.conf /etc/nginx/sites-available/saswat_cust_app
chmod 710 /var/lib/jenkins/workspace/02_DJango_CustApp_CICD

sudo ln -s /etc/nginx/sites-available/saswat_cust_app /etc/nginx/sites-enabled
sudo nginx -t

sudo systemctl start nginx
sudo systemctl enable nginx

echo "Nginx has been started"

sudo systemctl status nginx