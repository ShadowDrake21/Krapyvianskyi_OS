#!/bin/bash

count=$(find "/etc" -type f ! -type d ! -type l 2>/dev/null | wc -l)

# result
echo "Number of files in folder /etc: $count"
