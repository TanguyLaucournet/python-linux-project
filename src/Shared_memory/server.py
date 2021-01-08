import numpy as np
a = np.array([1, 1, 2, 3, 5, 8])  # Start with an existing NumPy array
from multiprocessing import shared_memory
shm = shared_memory.SharedMemory(create=True, size=a.nbytes,name='psm_957212c1')
# Now create a NumPy array backed by shared memory
b = np.ndarray(a.shape, dtype=a.dtype, buffer=shm.buf)
b[:] = a[:]  # Copy the original data into shared memory
print(b)

type(b)

type(a)

print(shm.name) # If we did not specify a name one would be chosen for us and we would have to paste it in the client
wait =input('Launch client then press enter')
print(b)

# Clean up from within the first Python shell
del b  # Unnecessary; merely emphasizing the array is no longer used
shm.close()
shm.unlink()  # Free and release the shared memory block at the very end