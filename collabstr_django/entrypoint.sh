#!/bin/bash

# Wait for the database to be ready (optional)
# You can add logic here to wait for your database to be fully started
# This can be important in production environments

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Run the seed script
echo "Running seed script..."
python seed.py

# Start the main process
echo "Starting Django server..."
exec "$@"