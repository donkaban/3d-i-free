#!/bin/bash
cd ./python
rm -rf ./dist
python ./setup.py py2app
rm -rf ./build
cp -R ../data ./dist/miniGL.app/Contents/