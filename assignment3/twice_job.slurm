<<<<<<< HEAD




echo " " 
echo "Calling twice.sh"
./twice.sh 

srun ./twice.sh 5

srun ./twice.sh 2

srun ./twice.sh 7

srun ./twice.sh 6

srun ./twice.sh 1

srun ./twice.sh 3
=======
#!/bin/bash

#Run_1

#SBATCH --nodes=1
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



#Run_3

#SBATCH --nodes=2
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=40
#SBATCH -p compute2
#SBATCH -t 00:05:00

./twice.sh 5 &
./twice.sh 2 &
./twice.sh 7 &
./twice.sh 6 &
./twice.sh 1 &
./twice.sh 3

wait

echo "Job finished in $SECONDS seconds"


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

#Run_5

#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=8
#SBATCH -p amdonly
#SBATCH -t 00:05:00

./twice.sh 5 &
./twice.sh 2 &
./twice.sh 7 &
./twice.sh 6 &
./twice.sh 1 &
./twice.sh 3

wait

echo "Job finished in $SECONDS seconds"
>>>>>>> c8282cf560a29cfdde140c4a4deacdb6acb9c5ff

srun -p compute1 -N 1  -n 1 -c 4  -t 00:05:00 pty bash
