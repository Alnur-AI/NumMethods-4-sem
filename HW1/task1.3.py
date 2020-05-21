import numpy as np
import scipy.linalg as sl
import time
import random
import matplotlib.pyplot as plt

#//////ARRAY SIZES/////////#
arr_size = 34
A_size = np.linspace(100,100*arr_size, num = arr_size)
my_time = [0]*arr_size
np_time = [0]*arr_size



#////////Data Input////////#
def input_data(n):
	print('Creating A...')
	A = np.zeros((n, n))
	print('Make diagonals...')
	for a in range(0,n):
		for b in range(a - 1,a + 2):
			if (b == -1):
				A[a][0] = random.random()
				continue
			if (b == n):
				break
			A[a][b] = random.random()
		f = np.random.rand(n)
	x = [0] * n
	print('Done!')
	return A,f,x,n

#//////matrix for solve_banded////////////#
def s_banded_matr(A,n):
	print('Creating bca for solve_banded...')
	a = [0] * n
	b = [0] * n
	c = [0] * n
	for i in range(0,n):
		for j in range(i-1,i+2):
			if (j == i - 1 and j != -1):
				a[i-1] = A[i][j]
			if (j == i):
				c[i] = A[i][j]
			if (j == i + 1 and j != n):
				b[i+1] = A[i][j]
	print('Done!')	
	return np.array([b,c,a])



#//////START PROGRAM////////////#
for count in range(1,arr_size+1):


	print('ARRAY_SIZE: ', count*1000)
	A,f,x,n = input_data(count*1000)
	abc = s_banded_matr(A,n)


	#Numpy solution
	start_time = time.time()

	xx = sl.solve_banded((1,1), abc, f)

	np_time[count-1] = time.time() - start_time
	print('\nNP time:', np_time[count-1])
	



	#Start time for my solution
	start_time = time.time()

	#////My solution: creating upper triagular matrix
	#a - Sub-diagonal elements
	#b - Super-diagonal elements
	#c - Diagonal elements
	m = 1;	
	for i in range(1,n):
		m = A[i][i - 1]/A[i-1][i-1]#m = a[i]/c[i-1];
		A[i][i] = A[i][i] - m*A[i-1][i]#c[i] = c[i] - m*b[i-1]
		f[i] = f[i] - m*f[i-1]#f[i] = f[i] - m*f[i-1]

	#Finding x
	x[n-1] = f[n-1]/A[n-1][n-1];
	for i in range(n - 2, -1, -1):
	  x[i]=(f[i] - A[i][i + 1]*x[i+1]) / A[i][i]

	#Output my time
	my_time[count-1] = time.time() - start_time
	print('My time:', my_time[count-1])

	#Output
	print('\n||x - xx|| = ', max(np.absolute(x-xx)) )
	print ('SAME? ANSWER:', np.allclose(x,xx), '\n\n\n\n\n\n\n\n\n\n\n\n')

plt.title('tridiagonal algorithm results')
plt.plot (A_size, np_time , label = 'Numpy')
plt.plot (A_size, my_time , label = 'Tridiagonal method')
plt.legend()
plt.ylabel('Seconds')
plt.xlabel('Matrix size')
plt.show ()
