#!/usr/bin/env bash

echo "Waiting for MySQL..."

while ! nc -z sql 3306; do
  sleep 0.5
done

echo "MySQL started"

flask sql init
flask sql migrate
flask sql upgrade

cd /Photos-Docker-Flask
python run.py