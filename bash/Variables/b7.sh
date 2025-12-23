#!/bin/bash

read -p "Enter your name: " NAME
read -p "Enter your birth year: " BIRTHYEAR

CURRENT_YEAR=$(date +"%Y")
AGE=$((CURRENT_YEAR - BIRTHYEAR))

echo "${NAME}, you are approximately ${AGE} years old"
