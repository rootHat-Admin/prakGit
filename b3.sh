#!/bin/bash

echo "Hello, $(whoami)! To day $(date)"

for file in * .py; do
    echo "File: $file"
done
