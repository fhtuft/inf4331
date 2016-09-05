#!/bin/bash -x

# Parse commandline options #
if [ "$1" ==  "--AMPM" ]; then
    options="%r"
else
    options="%T"
fi

# Print time #
while true
do
    date +$options
    sleep 1
done
