#!/bin/bash 

# Parse commandline options #
if [ "$1" ==  "--AMPM" ]; then
    options="%r"
else
    options="%T"
fi

# Print time #
while true
do
    printf "\033c"
    date +$options
    sleep 1
done
