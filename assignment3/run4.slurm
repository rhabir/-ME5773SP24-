#!/bin/bash

#Run_4

#SBATCH --nodes=4
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=80
#SBATCH -p compute1
#SBATCH -t 00:05:00

./twice.sh 5 &
./twice.sh 2 &
./twice.sh 7 &
./twice.sh 6 &
./twice.sh 1 &
./twice.sh 3

wait

echo "Job finished in $SECONDS seconds"
