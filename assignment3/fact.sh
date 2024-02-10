#!/bin/bash

# Get input number
read -p "Enter a number: " N

# Initialize factorial 
fact=1 

# Compute and output factorials up to N
for ((i=1; i<=N; i++)); do

  fact=$((fact * i))
  
  echo "$i! = $fact"
  
done
