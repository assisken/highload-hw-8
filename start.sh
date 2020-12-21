#!/bin/bash

python3 replace_docker_ip.py
docker-compose up -d zookeeper
sleep 2
docker-compose up
