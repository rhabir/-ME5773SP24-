#!/bin/bash

#SBATCH -J multProcPy
#SBATCH -o HW10_outFile.%j.txt    # Name of 'stdout' output file.
#SBATCH -e errFile.%j.txt    # Name of 'stderr' error file.
#SBATCH -p compute1          # Partition
#SBATCH -N 1                 # Total number of nodes to be requested.
#SBATCH -n 1                 # Total number of tasks to be requested.
#SBATCH -c 80                # Number of threads used by each task, adjust if necessary.
#SBATCH -t 02:00:00          # Maximum estimated run time (dd-hh:mm:ss)
#SBATCH --mail-type=ALL      # Mail events to notify (END, FAIL, ALL).
#SBATCH --mail-user rakib.hasan@utsa.edu


# Load necessary modules
module load intel/oneapi

# Set the environment variable for OpenMP
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

ulimit -s unlimited

# Compile the program
make

# Execute with different numbers of threads
for threads in 1 2 4 8 16; do
    echo "Running with $threads threads:"
    export OMP_NUM_THREADS=$threads
    ./main_program.exe  # Ensure ntasks is specified directly
done
