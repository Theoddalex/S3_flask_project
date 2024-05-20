#!/bin/sh

# Initialize the database if it hasn't been initialized yet
if [ ! -d "migrations" ]; then
  flask db init
fi

# Run database migrations
flask db migrate
flask db upgrade

# Execute the CMD from the Dockerfile
exec "$@"
