#!/bin/bash

rsync -r docker-compose.yaml nginx swarm-manager:

ssh swarm-manager docker stack deploy --compose-file docker-compose.yaml Password

