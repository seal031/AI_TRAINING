import numpy as np

a=np.arange(0,12,dtype = np.int16)
b=a.reshape(3,4)
print(b)
print(b.ndim)
print(b.itemsize)

x=np.linspace(0,10,5,False)
print(x)
x=np.logspace(1,10,num=10,base=2)
print(x)

a = np.arange(10)
s = slice(2,7,2)
print(a)
print(a[s])
b = a[2:7:2]
print(b)
print(a[1::3])

a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a[:,1:])