#!/bin/bash

#SBATCH -J multProcPy
#SBATCH -o numInt_outFile.%j.txt    # Name of 'stdout' output file.
#SBATCH -e errFile.%j.txt    # Name of 'stderr' error file.
#SBATCH -p compute1          # Partition
#SBATCH -N 1                 # Total number of nodes to be requested.
#SBATCH -n 1                 # Total number of tasks to be requested.
#SBATCH -c 80                # Number of threads used by each task, adjust if necessary.
#SBATCH -t 00:20:00          # Maximum estimated run time (dd-hh:mm:ss)
#SBATCH --mail-type=ALL      # Mail events to notify (END, FAIL, ALL).
#SBATCH --mail-user rakib.hasan@utsa.edu

echo Starting job - `date`

# Setup environment
module load anaconda3
source activate hpc

# Array of thread counts to test
threads=(1 2 4 8 16 20)

for t in "${threads[@]}"
do
    echo "Running with NUMBA_NUM_THREADS=$t"
    export NUMBA_NUM_THREADS=$t
    tstart=`date +%s%N`  # Start time
    
    # Run the python script
    python3 numInt.py
    
    tend=`date +%s%N`  # End time
    tdiff=$(( (tend-tstart)/1000000 ))  # Calculate duration
    echo "Calculations ended with NUMBA_NUM_THREADS=$t"
    echo "Total CPU time $tdiff [ms]"
    echo "----------------------------------"
done
