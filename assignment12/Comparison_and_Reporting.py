import cupy as cp
import time as time
import numpy as np

'''
print ("Matrix K: [[ 4. -2.  0. ...  0.  0.  0.]
 [-2.  4. -2. ...  0.  0.  0.]
 [ 0. -2.  4. ...  0.  0.  0.]
 ...
 [ 0.  0.  0. ...  4. -2.  0.]
 [ 0.  0.  0. ... -2.  4. -2.]
 [ 0.  0.  0. ...  0. -2.  2.]]

Matrix f: [0.00000000e+00 0.00000000e+00 0.00000000e+00 ... 0.00000000e+00
 0.00000000e+00 3.33333333e-05]

Solution vector u:
[1.66666667e-05 3.33333333e-05 5.00000000e-05 ... 4.99966667e-01
 4.99983333e-01 5.00000000e-01]

Value of u[N-1]: 0.4999999998518403

CPU time(CUDA): 6.958054065704346 seconds")



print ("Matrix K: [[ 4. -2.  0. ...  0.  0.  0.]
 [-2.  4. -2. ...  0.  0.  0.]
 [ 0. -2.  4. ...  0.  0.  0.]
 ...
 [ 0.  0.  0. ...  4. -2.  0.]
 [ 0.  0.  0. ... -2.  4. -2.]
 [ 0.  0.  0. ...  0. -2.  2.]]

Matrix f: [0.00000000e+00 0.00000000e+00 0.00000000e+00 ... 0.00000000e+00
 0.00000000e+00 3.33333333e-05]

Solution vector u (CPU):
[1.66666667e-05 3.33333333e-05 5.00000000e-05 ... 4.99966667e-01
 4.99983333e-01 5.00000000e-01]

Value of u[N-1] on CPU: 0.4999999998518403

CPU execution time (NumPy): 13.316904306411743 seconds")
'''


CPU_time_GPU_CUDA = 6.958054065704346 
CPU_execution_time_NumPy = 13.316904306411743


speedup = CPU_execution_time_NumPy / CPU_time_GPU_CUDA

print("Speedup (GPU over CPU):", speedup, "times")