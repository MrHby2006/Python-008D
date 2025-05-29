
from random import randint
import time

d1 = randint(1,12)

posiciónP1 = 0
posiciónP2 = 0 

nombreP1 = input("Ingrese el nombre del jugaror 1: ")
nombreP2 = input("Ingrese el nombre del jugaror 2: ")

while posiciónP1 < 100 or posiciónP2  < 100:
    print(f"{nombreP1} lanza el dado y avanza {d1} casilla/s")
    posiciónP1 = posiciónP1 + d1
    print(f"{nombreP1} esta en la casilla {posiciónP1}")
    time.sleep(5)
    print(f"{nombreP2} lanza el dado y avanza {d1} casilla/s")
    posiciónP2 = posiciónP2 + d1
    print(f"{nombreP2} esta en la casilla {posiciónP2}")
    time.sleep(5)