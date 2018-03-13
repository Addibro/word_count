#!/bin/bash

if [ $# == 1 ]; then
    echo "Looking for the ten most occurring words"
    echo ""
    python wordcount.py $1 0
elif [ $# == 2 ]; then  
    echo "Looking for the ten most occurring words with $2 or more characters"
    echo ""
    python wordcount.py $1 $2
fi