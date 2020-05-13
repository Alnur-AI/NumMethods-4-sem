import numpy as np
import math
import time
import matplotlib . pyplot as plt

size = 5
start_time = time.time()
my_time = [0]*size
np_time = [0]*size

for count in range(1,size+1):

	print('MATRIX SIZE: ', count*100)

	#////////ВВОД ДАННЫХ/////////#
	n = 100*count
	L = np.tril(np.random.rand(n, n))
	for i in range(0,n):
		L[i][i] = 456
	A = L.dot(np.transpose( L ))
	f = np.random.rand(n)
	x = [0] * n
	#////////////////////////////#

	#РЕШЕНИЕ ОТ NUMPY
	S = np.linalg.cholesky(A)
	np_time[count - 1] = time.time() - start_time
	print('NUMPY TIME: ', np_time[count - 1])

	#ОБЬЯВЛЯЕМ НИЖНЕТРЕУГОЛЬНУЮ МАТРИЦУ L ДЛЯ РАЗЛОЖЕНИЯ ХОЛЕЦКОГО МАТРИЦЫ А
	L = np.tril(np.random.rand(n, n))

	#ОБНОВЛЯЕМ ВРЕМЯ ДЛЯ РАСЧЕТА ВРЕМЕНИ СОБСТВЕННОГО МЕТОДА
	start_time = time.time()

	#МОЙ МЕТОД ХОЛЕЦКОГО
	s = 0;
	for j in range(0,n):
		for i in range(j,n):
			s = 0;
			if (i == j):
				for k in range(0,j):
					s += (L[j][k] * L[i][k])
				if (A[j][i] - s <= 0):
					print ('IMPOSSIBLE. NEGATIVE ORIENTATION. NO CHANGES.\n')
				L[i][j] = math.sqrt(A[j][i] - s)
				continue
			for k in range(0,j):
				s += L[j][k]*L[i][k]
			if (A[j][j] == 0):
				print ('IMPOSSIBLE. NEGATIVE ORIENTATION. [L] NOW EQUAL ZERO.\n')
			L[i][j] = (A[j][i] - s)/L[j][j];

	#СКОЛЬКО ВРЕМЕНИ УШЛО НА МОЙ АЛГОРИТМ?
	my_time[count - 1] = time.time() - start_time
	print('MY TIME: ', my_time[count - 1])

	#ПРОВЕРКА РЕШЕНИЯ
	A = L.dot(np.transpose( L ))
	B = S.dot(np.transpose( S ))
	print ('SAME? ANSWER:', np.allclose(A,B), '\n')
	#//#\\print ('A = \n', A, '\n\n\n' , 'L = \n',L)

plt.plot(my_time)
plt.plot(np_time)
plt.show()
