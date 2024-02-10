#!/bin/bash

# Get input number as script argument 
input=$1

# Calculate sleep time
sleep_time=$((2*$input))

# Sleep 
sleep $sleep_time

# Print output message
echo "Terminated a task that takes $sleep_time seconds."
