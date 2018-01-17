#!/bin/bash

echo '###############################'
echo "Preparing..."
echo '###############################'

sudo rm -rvf ./webapi
mkdir ./webapi
cp -Rvf ../model ./webapi/
cp -Rvf ../api ./webapi/
cp -Rvf ../wicket ./webapi/
cp ../*.py ./webapi/

echo '###############################'
echo "Building webapi"
echo '###############################'
docker run -it --name webapi-builder --rm -v $(pwd)/webapi:/webapi/ webapi /bin/sh -c "python -m compileall /webapi -b"

echo '###############################'
echo "Packing webapi"
echo '###############################'
rm -rvf webapi/*.py
rm -rvf webapi/*/*.py
rm -rvf webapi/*/__pycache__

tar -zcvf webapi.tgz webapi
