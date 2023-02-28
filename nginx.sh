#!/bin/bash

sudo cp -rf app.conf /etc/nginx/sites-available/.
chmod 710 /var/lib/jenkins/workspace/mesotheliomalegalhelpcenter

sudo ln -s /etc/nginx/sites-available/. /etc/nginx/sites-enabled
sudo nginx -t

sudo systemctl start nginx
sudo systemctl enable nginx

echo "Nginx has been started"

sudo systemctl status nginx
