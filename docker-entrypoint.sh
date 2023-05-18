#!/bin/sh


case $1 in
    bootstrap)
      # Waits for database to completely be ready for new connections
      sleep 5
      # Apply database migrations
      echo "Apply database migrations"
      python manage.py migrate
      ;;
    rungunicorn)
      # Start server
      echo "Starting gunicorn server"
      gunicorn --workers=1 --bind=0.0.0.0:8000 moberries_challenge.wsgi:application
      ;;
    *)
      echo "Unknown command"
      exit 1
      ;;
esac
