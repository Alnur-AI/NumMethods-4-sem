import numpy as np
import scipy.linalg as sl
import time
import random
import matplotlib . pyplot as plt

#//////РАЗМЕР МАССИВА/////////#
print('Input x vector size: ')
arr_size = 25
my_time = [0]*arr_size
np_time = [0]*arr_size
print('\n')

for count in range(1,arr_size+1):
	#////////ВВОД ДАННЫХ////////#
	def input_data(n):
		print('Creating A...')
		A = np.zeros((n, n))
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

	#//////МАТРИЦА ДЛЯ solve_banded////////////#
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



	#//////НАЧИНАЕМ ВЫПОЛНЯТЬ ПРОГРАММУ ////////////#
	print('ARRAY_SIZE: ', count*1000)
	A,f,x,n = input_data(count*1000)
	abc = s_banded_matr(A,n)

	start_time = time.time()

	xx = sl.solve_banded((1,1), abc, f)

	np_time[count-1] = time.time() - start_time
	print('\nNP time:', np_time[count-1])
	start_time = time.time()



	#Мой прямой ход
	m = 1;
	#a - поддиагональные элементы
	#b - наддиагональные элементы
	#c - диагональные элементы
	for i in range(1,n):
		m = A[i][i - 1]/A[i-1][i-1]#m = a[i]/c[i-1];
		A[i][i] = A[i][i] - m*A[i-1][i]#c[i] = c[i] - m*b[i-1]
		f[i] = f[i] - m*f[i-1]#f[i] = f[i] - m*f[i-1]

	#Мой обратный ход
	x[n-1] = f[n-1]/A[n-1][n-1];
	for i in range(n - 2, -1, -1):
	  x[i]=(f[i] - A[i][i + 1]*x[i+1]) / A[i][i]

	my_time[count-1] = time.time() - start_time
	print('My time:', my_time[count-1])

	#Вывод
	print('\n||x - xx|| = ', max(np.absolute(x-xx)) )
	print ('SAME? ANSWER:', np.allclose(x,xx), '\n\n\n\n\n\n\n\n\n\n\n\n')

plt.plot(my_time)
plt.plot(np_time)
plt.show()
