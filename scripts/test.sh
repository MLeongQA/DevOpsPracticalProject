#!/bin/bash

source venv/bin/activate
pip3 install -r requirements.txt

python3 -m pytest --cov=. --cov-report=term-missing

