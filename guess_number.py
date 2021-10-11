#User has to guess a random number generated (between 1 and 10) by this program.
import random
import time

n=random.randint(1,10)
respuesta=int(input("Dime un número y prueba\n"))

if respuesta!=n:
    print("Lo siento has fallado")

if respuesta>10:
    print("Te has pasado\n")


else: print("Enhorabuena, has acertado!")
time.sleep(10)