#!/bin/bash

docker ps -a | tr -s ' ' | tail +2 | cut -d' ' -f1 | xargs docker rm --force
python3 replace_docker_ip.py

docker-compose up -d zookeeper
sleep 5
docker-compose up
