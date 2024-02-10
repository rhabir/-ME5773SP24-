#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1  
#SBATCH -c 1

# Run twice.sh with input 5  
srun ./twice.sh 5

# Run twice.sh with input 2
srun ./twice.sh 2

# Run twice.sh with input 7
srun ./twice.sh 7

# Run twice.sh with input 6 
srun ./twice.sh 6

# Run twice.sh with input 1
srun ./twice.sh 1 

# Run twice.sh with input 3
srun ./twice.sh 3

