#!/bin/bash

pip freeze --local | grep -v flaskee > requirements.txt