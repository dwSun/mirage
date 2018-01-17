#!/bin/bash

echo '###############################'
echo "Preparing..."
echo '###############################'
cp ../requirements.txt ./
docker build --rm -t webapi .
