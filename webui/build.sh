#!/bin/bash

echo '###############################'
echo "Preparing..."
echo '###############################'

rm -rvf ./dist
rm -rvf ./webui

npm install

echo '###############################'
echo "Building webui src"
echo '###############################'
npm run build

echo '###############################'
echo "Packing webui"
echo '###############################'
mkdir -p ./webui/dist

cp favicon.ico webui
cp index-build.html webui/index.html
cp -Rvf ./dist/*.js ./webui/dist

tar -cvzf webui.tgz webui/
