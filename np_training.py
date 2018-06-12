import numpy as np

a=np.arange(0,12,dtype = np.int16)
b=a.reshape(3,4)
print(b)
print(b.ndim)
print(b.itemsize)

a = np.arange(0,60,5)
a = a.reshape(3,4)
b=a.T
print(a)
print(b)

a = np.arange(0,60,5)
a = a.reshape(3,4)
print('原始数组是：')
print (a )
for x in np.nditer(a, op_flags=['readwrite']):
    x[...]=2*x
print('修改后的数组是：')
print(a)

a = np.arange(8).reshape(2,4)
print(a.flatten(order = 'k'))