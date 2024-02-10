#!/bin/bash


#Run_2


#SBATCH --nodes=1
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=40
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
