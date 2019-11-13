# Descripción: Reversi es un cásico juego de mesa.
# Autores: Angel Rodriguez, Kevin Briceño
# Fecha de modificación: 12/11/2019
# Variables:
# jugador1
# jugador2
# i: int // cordenada para la fila
# j: int // cordenada para la columna
# reversi: list // Es el tablero de juego
# 0 // Casillas vacias
# 1 // casillas blacas
# 2 // casillas Negras
import random
class Jugardor():
	nombre=""
	ficha=0
class Cordenadas():
	i=0
	j=0
def imprimir(tablero:[int])->"void":
	for i in tablero:
		print(i)
def incio(tablero:[int])->list:
	tablero[3][3]=1
	tablero[3][4]=2
	tablero[4][3]=2
	tablero[4][4]=1
	return tablero

jugador1=Jugardor()
jugador2=Jugardor()
jugador1.nombre=random.choice(["Ale","Kevin","luisa", "Kathe","chang"])#input("Nombre del jugador1: ")
jugador2.nombre=random.choice(["Ale","Kevin","luisa", "Kathe","chang"])#input("Nombre del jugador2: ")
jugador1.ficha=1
jugador2.ficha=2		
reversi=[[0 for j in range(0,8)]for i in range(0,8)]
incio(reversi)
print("los nombres dados son: ",jugador1.nombre, jugador2.nombre)
print(jugador1.ficha, jugador2.ficha)
imprimir(reversi)