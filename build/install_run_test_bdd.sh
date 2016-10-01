#!/usr/bin/env bash

virtualenv venv
. venv/bin/activate

pip install -r requirements.txt
pip install -e .

lettuce vm/test/ --with-xunit
