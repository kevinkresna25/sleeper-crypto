#!/usr/bin/env bash
docker-compose down -v
docker image prune -f
docker-compose up -d --build
