#!/bin/bash

# Check if an argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 DAY"
    exit 1
fi

DAY=$1
FILENAME="day${DAY}.py"

# Check if the file exists
if [ ! -f "$FILENAME" ]; then
    echo "File $FILENAME does not exist."
    exit 1
fi

# Commit and push the file
git add $FILENAME
git commit -m "Day $DAY (1 + 2)"
git push