#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Download postal data
python download_postal_data.py

# Create data directory if it doesn't exist
mkdir -p data