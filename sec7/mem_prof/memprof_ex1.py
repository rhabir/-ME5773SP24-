import numpy as np
from memory_profiler import profile
import time

def smallmem_funct(size):
    res  = np.empty((size,3))
    res[:] = 1.0
    return res

# end function

def bigmem_funct(size):

    res  = np.empty((size,size))
    res[:,:] = 0.0
    return res

# end function

@profile
def main():

    size1 = 5_000_000
    size2 =    50_000

    res = smallmem_funct(size1)

    res = bigmem_funct(size2)

    del res

    return 

# end function

if __name__=="__main__":

    main()
    
# end if 