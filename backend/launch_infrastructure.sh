#!/bin/bash

echo $1
cd $1

docker-compose rm -fn
docker-compose build
docker-compose up
