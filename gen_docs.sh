#!/bin/bash

export PYTHONPATH=$PWD/waro

mkdir -p docs
cd docs

pydoc -w ../waro

cd ..

echo "browse to file:///$PWD/docs/"
echo "Ready."
