#!/bin/bash

# Get input
read -p "Enter a number: " N

# Calculate sleep time 
sleep_time=$((2*N))

# Sleep for calculated time
sleep $sleep_time

# Print output message
echo "Terminated a task that takes $sleep_time seconds."
