#!/bin/bash

echo $1
cd $1

echo $2

if [ -n "$2" ]
then
  echo '1'
  docker-compose down
else
  docker-compose down
  docker-compose build
  docker-compose up
  echo '1'
fi
