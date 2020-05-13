import numpy as np
from math import *
import scipy.linalg as sla
import time 
import matplotlib.pyplot as plt

eps = 1000000
size = 5 #size*100 - размер матрицы
my_time = [0]*size
np_time = [0]*size

def zeidel(n, A, f, x):
	xnew = np.zeros(n)
	for i in range(n):
		s = 0
		for j in range(i):
			s = s + A[i][j] * xnew[j]
		for j in range(i+1, n):
			s = s + A[i][j] * x[j]
		xnew[i] = (f[i] - s) / A[i][i]
	return xnew

def diff(n, x, y):
	s = 0
	for i in range(n):
		s += (x[i] - y[i]) ** 2
	return sqrt(s)

def solve(n, A, f):
	xnew = np.zeros(n)
	while True:
		x = np.array(xnew)
		xnew = zeidel(n, A, f, x)
		if diff(n, x, xnew) < eps:
			break
	return xnew

for count in range(1,size+1):
	#Вводные данные: n, A, A_np, f, f_np
	n = count*100		
	A = np.random.rand(n,n)
	
	s = np.sum(np.abs(A), axis = 1)
	for i in range(n):
		A[i][i] = A[i][i] + s[i]
	
	A_np = np.array(A)
	f = np.random.rand(n)
	f_np = np.array(f)

	#Значение эпсилона и размера матрицы
	print('epsilon = ',eps)
	print('n = ', n)

	#Мой метод
	start = time.time()
	x = solve(n, A, f)
	my_time[count - 1] = time.time() - start
	print('My time: ',my_time[count - 1])

	#Метод numpy
	start = time.time()
	x_np = np.linalg.solve(A_np, f_np)
	np_time[count - 1] = time.time() - start
	print('NP time: ',np_time[count - 1])
	
	#Одинаковы ли решения?
	print('\n||x - x_np|| = ', max(np.absolute(x_np-x)) )
	print ('\n\n\n\n\n')

#Вывод графика
plt.plot(my_time)
plt.plot(np_time)
plt.show()
