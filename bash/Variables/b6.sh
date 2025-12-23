#!/bin/bash

read -p "Enter your name: " USERNAME
NOWTIME=$(date +"%H:%M")
echo "User ${USERNAME} logged in at ${NOWTIME}"