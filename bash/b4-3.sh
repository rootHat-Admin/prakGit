#!/bin/bash
# script with user input and exit code 

read -p "Enter IP address to pong: " IP
ping -c 1 $IP > /del/null

if [ $? -eq 0 ]; then
    echo "Host $IP is reachable"
else
    echo "Host $IP is not reachable"
fi