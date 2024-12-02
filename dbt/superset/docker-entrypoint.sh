#!/bin/bash

set -e

# Wait for the database to be ready
echo "Waiting for PostgreSQL..."
while ! nc -z superset-postgres 5432; do
  sleep 1
done
echo "PostgreSQL is up!"

# Initialize Superset database
echo "Running Superset DB upgrade..."
superset db upgrade

# Create an admin user (only if not already created)
if ! superset fab list-users | grep -q "admin"; then
  echo "Creating admin user..."
  superset fab create-admin \
    --username "${ADMIN_USERNAME:-admin}" \
    --firstname "${ADMIN_FIRSTNAME:-Phi}" \
    --lastname "${ADMIN_LASTNAME:-Nguyen}" \
    --email "${ADMIN_EMAIL:-admin@example.com}" \
    --password "${ADMIN_PASSWORD:-admin}"
fi

# Initialize Superset
echo "Initializing Superset..."
superset init

# Run Superset server
superset run --host=0.0.0.0 --port=8088