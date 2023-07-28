import numpy as np

a = np.array([1,2,3])
print(a)

b = np.zeros(2)
print(b)

c = np.ones(3)
print(c)

d = np.empty(2)
print(d)

e = np.arange(5)
print(e)

f = np.arange(2, 9, 2) #First, last, step
print(f)

g = np.linspace(0, 10, num=5)
print(g)

h = np.ones(2, dtype = np.int64)
print(h)

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print(np.sort(arr))

j = np.array([5, 7, 9, 0])
k = np.array([3, 8, 1, 4])
i = np.concatenate((j, k))
print(i)

l = np.array([[1, 2], [3, 4]])
m = np.array([[5, 6]])
o = np.concatenate((l, m), axis=0)
print(o)


arr2 = np.array([[[0, 1, 2, 3],
                  [4, 5, 6, 7]],

                 [[0, 1, 2, 3],
                  [4, 5, 6, 7]],

                 [[0 ,1 ,2, 3],
                  [4, 5, 6, 7]]])
print(np.ndim(arr2))
print(np.size(arr2))
print(np.shape(arr2))

arr3 = arr2.reshape(1, 24)
print(arr3)
p = np.arange(6)
print(p)
q = p.reshape(3, 2)
print(q)

r = np.array([[0, 1],
              [2, 3],
              [4, 5]])
s = np.reshape(r, newshape=(1, 6), order='C')
print(s)