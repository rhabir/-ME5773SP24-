



echo " " 
echo "Calling twice.sh"
./twice.sh 

srun ./twice.sh 5

# Print hello world to ouptut file.
echo "HELLO WORLD"

# Print hello world using the srun command
srun echo "hello world"

echo " " 
echo "Calling run.sh"
./run.sh

echo " "
echo "Calling run.sh with the srun command."

srun -p compute1 -N 1 -n 2 -t 00:05:00 -c 4  ./run.sh
