#!/bin/bash
#SBATCH --partition=compute1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=80
#SBATCH --time=5:00
#SBATCH --output=output_%j.txt

module load anaconda3
conda activate envTeam4

for threads in 1 2 4 8 16 20 40
do
    export MKL_NUM_THREADS=$threads
    echo "Running with MKL_NUM_THREADS=$threads"
    python3 linalg.py
done

