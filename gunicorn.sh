#!/bin/bash

source env/bin/activate

cd /var/lib/jenkins/workspace/mesotheliomalegalhelpcenter

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --no-input

echo "Migrations done"

cd /var/lib/jenkins/workspace/mesotheliomalegalhelpcenter
cp -fr gunicorn.socket /etc/systemd/system/
cp -fr gunicorn.service /etc/systemd/system/

echo "$USER"
echo "$PWD"



/usr/bin/systemctl daemon-reload
/usr/bin/systemctl start gunicorn

echo "Gunicorn has started."

systemctl enable gunicorn

echo "Gunicorn has been enabled."

/usr/bin/systemctl restart gunicorn


/usr/bin/systemctl status gunicorn

