#!/bin/bash

set -e

sudo chown -R mysql:mysql /var/lib/mysql/.

docker-compose build --parallel && \
#docker login -u ${DOCKERHUB_CREDENTIALS_USR} -p ${DOCKERHUB_CREDENTIALS_PSW}
docker login -u mleongqa -p QACTrainee1
docker-compose push