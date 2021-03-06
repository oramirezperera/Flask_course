#!/bin/bash

source venv/bin/activate
pip3 install -r requirements.txt
source venv/bin/activate

export FLASK_APP=main.py
export FLASK_DEBUG=1
export FLASK_ENV=development

flask run