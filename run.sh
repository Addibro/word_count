#!/bin/bash

if [ $# == 1 ]; then
    python wordcount.py $1 0
elif [ $# == 2 ]; then  
    python wordcount.py $1 $2
fi