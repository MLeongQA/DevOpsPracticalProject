#!/bin/bash

rsync -r docker-compose.yaml nginx swarm-manager:

ssh swarm-manager "export DATABASE_URI=${DATABASE_URI} && export SECRET_KEY=${SECRET_KEY} && docker stack deploy --compose-file docker-compose.yaml Password"

