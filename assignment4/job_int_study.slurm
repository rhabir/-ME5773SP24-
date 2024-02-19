#!/bin/bash
<<<<<<< HEAD


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

=======
#SBATCH --partition=compute1  
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=80
#SBATCH --output=integral_threads_%j.txt 
#SBATCH --time=02:50:00

module load anaconda3
conda activate envTeam4

for threads in 1 2 4 8; do
   export OMP_NUM_THREADS=$threads
      echo "Running with OMP_NUM_THREADS=$threads"
   export NUMEXPR_NUM_THREADS=$threads
      echo "Running with NUMEXPR_NUM_THREADS=$threads"
   python integral.py
done
>>>>>>> 5869bc22836099f66ad2dc3131be58cdfd7b121a
