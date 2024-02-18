#!/bin/bash


#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=80
#SBATCH -p compute1
#SBATCH -t 00:05:00

module load anaconda3
source activate envTeamX


for THREADS in 1 2 4 8
do
    export OMP_NP_THREADS=1
    export NUMEXPR_NUM_THREADS=1
    python3 integral.py
done

