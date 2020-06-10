import numpy as np
import time
import matplotlib.pyplot as plt

A_size = np.linspace(100,600, num = 6)
np_time = np.zeros(6)
my_time = np.zeros(6)

for tm in range (1,6+1):

	#////START TIME COUNT///#
	start_time = time.time()

	#////////Input matrix/////////#
	n = tm * 100
	A = np.random.rand(n, n)
	f = np.random.rand(n)
	x = np.zeros(n)
	#/////////////////////////////#



	#//////Solution from NUMPY//////#
	xx = np.linalg.solve(A, f)
	#///////////////////////////////#



	print(tm*100, 'x', tm*100, ' equation\n')
	print('numpy time:', time.time()-start_time, '\n')
	np_time[tm-1] = time.time()-start_time
	start_time = time.time()



	#/Make matrix upper triagular type/#
	for k in range(n):
		f[k] = f[k] / A[k][k]
		A[k] = A[k] / A[k][k]
		for i in range(k + 1, n):
			f[i] = f[i] - f[k] * A[i][k]
			A[i] = A[i] - A[k] * A[i][k]
			A[i][k] = 0
	#//////////////////////////////////#



	#Finding x
	for i in range(n - 1, -1, -1):
		x[i] = f[i]
		for j in range(i + 1, n):
			x[i] = x[i] - A[i][j] * x[j]
	#///////////////////////////////////////////#



	print('My algorithm time:', time.time()-start_time, '\n')
	my_time[tm-1] = time.time()-start_time

	print('Same solutions: ', np.allclose(x,xx))
	print('######################################################')

plt.title('Gauss results')
plt.plot (A_size, np_time , label = 'Numpy')
plt.plot (A_size, my_time , label = 'Gauss')
plt.legend()
plt.ylabel('Seconds')
plt.xlabel('Matrix size')
plt.show ()
