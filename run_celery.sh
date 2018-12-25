#!/bin/sh

# wait for RabbitMQ server to start
sleep 10

cd task
celery -A task worker -l info
