'''2. PreLab05Ejercicio2.py: Traduzca el algoritmo del ejercicio 1 a un programa en Python.
Para ello, lea N enteros, los coloque en un arreglo A y luego calcule la suma de los
elementos. Utilice la instrucción FOR para hacer el lazo. Se sugiere utilizar, la siguiente inicialización del arreglo A: 
A = [ int(input("A[" + str(i) + "]= ")) for i in range(0,N) ]'''



print("Sumador de Cadenas")

#Datos:
N = int(input("Coloque el numero de numeros a sumar : "))
A = [ int(input("A[" + str(i) + "]= ")) for i in range(0,N) ]

#Precondicion:
assert( N >= 0)

#Inicializacion:
suma = 0
i=0 

#Cota:
assert(N-i)

#Programa:
for i in A:
	#Invariante:
	assert(sum(A[i] for i in range(0,N)) )
	
	suma = suma + i

print("Este es el valor de la suma de la cadena : "+str(suma))

#Poscondicion:
assert(suma == sum(A[i] for i in range(0,N)))
