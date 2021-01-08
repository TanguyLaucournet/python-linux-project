import numpy as np
from multiprocessing import shared_memory
# Attach to the existing shared memory block
existing_shm = shared_memory.SharedMemory(name='psm_957212c1')
# Note that a.shape is (6,) and a.dtype is np.int64 in this example
c = np.ndarray((6,), dtype=np.int64, buffer=existing_shm.buf)

c[-1] = 888

print(c)


del c  # Unnecessary; merely emphasizing the array is no longer used
existing_shm.close()