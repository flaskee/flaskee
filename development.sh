#!/bin/bash

PWD=`pwd`
echo $PWD

activate () {
    . $PWD/venv/bin/activate
}

activate
sh ./serve.sh