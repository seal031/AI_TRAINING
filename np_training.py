import numpy as np

a=np.arange(0,12,dtype = np.int16)
b=a.reshape(3,4)
print(b)
print(b.ndim)
print(b.itemsize)