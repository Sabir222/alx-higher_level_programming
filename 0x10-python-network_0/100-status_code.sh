#!/bin/bash 
# script 
curl -s -L -X HEAD -w "%{http_code}" "$1"
