#!/bin/bash

echo "Python 3 version must be installed"
echo "To install python library run this script with parametr \"install\""

if [ -n "$1" ]; then
  if [[ "$1" == "install" ]]; then
    pip3 install --no-cache-dir -r requirements.txt
  fi
fi

python3 run.py