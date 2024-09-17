#!/bin/bash
set -e

# Update and install dependencies
apt-get update
apt-get install -y python3-pip git
pip3 install --upgrade pip
pip3 install poetry

# Clone the repository from GitHub
git clone https://github.com/rplis/get-attractions.git
cd get-attractions

# Install the package using Poetry
poetry config virtualenvs.create false
poetry install

# Run the application
poetry run get-attractions

# Wait for the service to start
sleep 10

# Check if the service is running and listening on port 8000
if netstat -tuln | grep ':8000'; then
    echo "Service is running and listening on port 8000"
else
    echo "Service is not running or not listening on port 8000"
    exit 1
fi