



echo " " 
echo "Calling twice.sh"
./twice.sh 

srun ./twice.sh 5

srun ./twice.sh 2

srun ./twice.sh 7

srun ./twice.sh 6

srun ./twice.sh 1

srun ./twice.sh 3

srun -p compute1 -N 1  -n 1 -c 4  -t 00:05:00 pty bash
