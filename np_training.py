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

x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])
# 对 y 广播 x
b = np.broadcast(x,y)

print('广播对象的形状：')
print(b.shape)

a = np.array([0,30,45,60,90])
print('不同角度的正弦值：')
# 通过乘 pi/180 转化为弧度
print(np.sin(a*np.pi/180)  )

a = np.array([-1.7,  1.5,  -0.2,  0.6,  10])
print(np.floor(a))
print(np.ceil(a))

a = np.array([[30,40,70],[80,20,10],[50,90,60]])
print(np.percentile(a,90,axis=0))
print(np.median(a,0))

x = np.array([3,  1,  2])
print(np.argsort(x))