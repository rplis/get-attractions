#!/bin/bash
apt-get update
apt-get install -y python3-pip
pip3 install --upgrade pip
pip3 install poetry
poetry config virtualenvs.create false
gsutil cp gs://YOUR_BUCKET_NAME/get_attractions-*.whl .
poetry install ./get_attractions-*.whl
poetry run get-attractions