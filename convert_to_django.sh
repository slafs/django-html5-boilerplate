#!/bin/bash

FILE=""
if [ -z "$1" ];then 
    echo "no file"
    echo "usage: $0 <path to html5boilerplate index.html file>"
    exit 1
else
    FILE=$1
fi

./boilerplate.convert.sed < $FILE > ./projectname/templates/base.html

