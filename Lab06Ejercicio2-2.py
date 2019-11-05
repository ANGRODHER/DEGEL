# Descripción: Programa que realiza la suma de todas la filas y todas la columnas de una matriz cuadrada
# Autor: Angel Rodriguez
# Fecha: 22/10/2019

# Variables:
# dimension: int // Entrada
# matriz: list of int // Entrada
# list1: list of int // Salida
# list2: list of int // Salida
# i : int // iterante
# j : int // iterante
# suma1: int // Contador
# suma2: int // Contador
import random
dimension=int(input("Ingrese la dimesión de la matriz cuadrada: "))
# Precondición
assert(dimension>=0)
#matriz=[[int(input("M["+str(i)+"]"+"["+str(j)+"]= "))for j in range(0,dimension)]for i in range(0,dimension)]
matriz=[[random.randint(-10,20) for j in range(0,dimension)]for i in range(0,dimension)]
print(matriz)

filas=[0 for i in range(0,dimension)]
columnas=[0 for i in range(0,dimension)]
suma1=0
suma2=0
# cota1= dimension-i
for i in range(0,dimension):
	# cota2= dimension-j
	# Verificaci´on del invariante en cada iteración
	assert((0<=i<dimension+1) and all(filas[k]==sum(matriz[k][j] for j in range(0,dimension))for k in range(0,i)))
	for j in range(0,dimension):
		# Verificación del invariante en cada iteración
		assert((0<=i<dimension+1) and all(filas[k]==sum(matriz[k][j] for j in range(0,dimension))for k in range(0,i))
		and all(columnas[k]==sum(matriz[j][k] for j in range(0,dimension)) for k in range(0,i)))
	
		suma1=suma1+matriz[i][j]
		suma2=suma2+matriz[j][i]
	filas[i]=suma1
	columnas[i]=suma2
	suma1=0
	suma2=0
# postcondición:
assert(all(filas[i]==sum(matriz[i][j] for j in range(0,dimension))for i in range(0,dimension))
and all(columnas[i]==sum(matriz[j][i] for j in range(0,dimension)) for i in range(0,dimension)))	
print("filas = ", filas)
print("columnas= ", columnas)