import numpy as np
import math
import time
import matplotlib.pyplot as plt

size = 3
start_time = time.time()

A_size = np.linspace(100,100*size, num = size)
my_time = np.zeros(size)
np_time = np.zeros(size)

for count in range(1,size+1):


	print('MATRIX SIZE: ', count * 100)

	#////////Input data//////////#
	n = 100 * count
	
	L = np.tril(np.random.rand(n, n))
	for i in range(0,n):
		L[i][i] = 42 #any positive number
	
	A = L.dot(np.transpose( L ))
	f = np.random.rand(n)
	x = np.zeros(n)
	#////////////////////////////#

	#Make lower triangular L to create A = LL^T
	L = np.zeros ((n , n))

	#START TIME
	start_time = time.time()	

	#NUMPY solution
	S = np.linalg.cholesky(A)
	np_time[count - 1] = time.time() - start_time
	print('NUMPY TIME: ', np_time[count - 1])




	#START TIME
	start_time = time.time()

	#MY CHOLESKY METHOD
	s = 0
	for j in range(0,n):
		for i in range(j,n):
			s = 0
			if (i == j):
				for k in range(0,j):
					s += (L[j][k] * L[i][k])
				L[i][j] = math.sqrt(A[j][i] - s)
				continue
			for k in range(0,j):
				s += L[j][k]*L[i][k]
			L[i][j] = (A[j][i] - s)/L[j][j]



	#Calculate my time
	my_time[count - 1] = time.time() - start_time
	print('MY TIME: ', my_time[count - 1])

	#My solution
	A = L.dot(np.transpose( L ))#My solution
	B = S.dot(np.transpose( S ))#numpy solution
	print ('SAME? ANSWER:', np.allclose(A,B), '\n')

plt.title('Cholesky results')
plt.plot (A_size, np_time , label = 'Numpy')
plt.plot (A_size, my_time , label = 'Cholesky')
plt.legend()
plt.ylabel('Seconds')
plt.xlabel('Matrix size')
plt.show ()
