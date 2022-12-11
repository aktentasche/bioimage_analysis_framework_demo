#!/bin/bash
# remove potential "old" container
docker rm bioimage-db-infra-redis
docker run --name bioimage-db-infra-redis redis