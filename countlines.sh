#!/bin/sh
echo 'PYTHON :'
wc -l `find ./python -name '*.py' `

echo 'C++ :'
wc -l `find ./mini_c++ -name '*.cpp' -o -name '*.h' `

