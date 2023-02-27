#!/bin/bash
if [ -d "env" ] 
then
    echo "Python virtual environment exists." 
else
    python -m venv env
fi

source env/bin/activate
python -m pip install --upgrade pip
python -m pip install --upgrade pillow


pip3 install -r requirements.txt

if [ -d "logs" ] 
then
    echo "Log folder exists." 
else
    mkdir logs
    touch logs/error.log logs/access.log
fi

sudo chmod -R 777 logs
