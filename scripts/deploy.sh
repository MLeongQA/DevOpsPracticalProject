#!/bin/bash

rsync -r docker-compose.yaml nginx swarm-manager:

ssh swarm-manager "export DATABASE_URI=${DATABASE_URI} && docker stack deploy --compose-file docker-compose.yaml Password"

