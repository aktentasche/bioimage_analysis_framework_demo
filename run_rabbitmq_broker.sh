#!/bin/bash
# remove potential "old" container
docker rm bioimage-db-infra-rabbit
# start RabbitMQ broker
docker run --hostname localhost --name bioimage-db-infra-rabbit -p 5672:5672 -p 15672:15672 -e RABBITMQ_DEFAULT_USER=biodude -e RABBITMQ_DEFAULT_PASS=biodude rabbitmq:3-management