#!/bin/bash
cd ./python
python ./setup.py py2app
#rm -rf ./build
cp -R ./data ./dist/main.app/Contents/Resources/