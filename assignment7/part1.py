from mpi4py import MPI
import numpy as np
import time
from gauleg import gauleg, f  # Ensure gauleg.py is in the same directory or in PYTHONPATH

def compute_integral(n, a, b):
    x = np.zeros(n)
    w = np.zeros(n)
    gauleg(a, b, x, w, n)
    integral = sum(w[i] * f(x[i]) for i in range(n))
    return integral

def main():
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    a, b = -1, 1  # Integration limits
    exact_result = 0.735758882342885 #-np.exp(1) + np.e, Exact result of the integral from -1 to 1

    if rank == 0:
        # Master process
        results = []
        start_time = time.time()
        for n in range(1, 21):
            worker = n  # Assuming 1 master and 20 workers
            comm.send(n, dest=worker, tag=1)
        for n in range(1, 21):
            integral, n, runtime = comm.recv(source=MPI.ANY_SOURCE, tag=2)
            percent_error = np.abs((integral - exact_result) / exact_result) * 100
            results.append((n, integral, percent_error, runtime))
        results.sort()  # Sort results by quadrature number
        print("Quadrature no.\tIntegration Result\tPercent error\tRun time (s)")
        for n, integral, percent_error, runtime in results:
            print(f"{n}\t{integral:.6f}\t{percent_error:.6f}\t{runtime:.6f}")
        total_time = time.time() - start_time
        print(f"Total execution time: {total_time:.6f} seconds")
    else:
        # Worker processes
        n = comm.recv(source=0, tag=1)
        start_time = time.time()
        integral = compute_integral(n, a, b)
        runtime = time.time() - start_time
        comm.send((integral, n, runtime), dest=0, tag=2)

if __name__ == "__main__":
    main()
