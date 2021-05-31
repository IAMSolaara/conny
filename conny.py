#autori Gabriele e il nonno Cauli 30/05/2021
import pygame
from console.screen import sc
from os import system
from keyboard import is_pressed
import time
from termcolor import cprint

row = 50
col = 150
posR = row//2
posC = col//2
old_posR = posR
old_posC = posC
points = []
colors = ["red","green","yellow","blue","magenta","cyan","white"]
index = 0
trash = []
rainbow = False

print("\u001b[2J")
with sc.location(0,0):
    print("SELECTED COLOR: ",end="")
    cprint("██",colors[index],end="")
    print("\t PRESS P TO PAINT",end="")
    print("\t PRESS C TO CHANGE COLOR",end="")
    print("\t PRESS F TO FOCUS",end="")
    print("\t PRESS X TO DELETE",end="")
    print("\t PRESS Z TO CLEAR",end="")
    print("\t PRESS R TO ACTIVATE/DEACTIVATE RAINBOW-MODE",end="")

while not(is_pressed("esc")):
    
    #pulizia dello schermo
    if is_pressed("z"):
        trash = points
        points = []   

    #cancellazione del punto dove si trova il cursore
    if is_pressed("x"):
        trash.append((posR,posC))
        for point in points:
            if posR == point[0] and posC == point[1]:
                points.remove(point)
            
    #porta fuori la spazzatura
    for point in trash:
        with sc.location(point[0],point[1]):
            print(" ")
    trash = []

    #on-off di rainbow mode
    if is_pressed("r"):
        rainbow = not rainbow

    #se la rainbow mode e' attiva
    if rainbow:
        #WOW I LIKE THIS RAINBOW
        index += 1 if index<6 else -6
        with sc.location(0,0):
            cprint("SELECTED COLOR: ██",colors[index],end="")

    #salva i punti quando 'p' e' premuto
    if is_pressed("p"):
        for point in points:
            #se il punto e' gia' presente lo rimuove
            if posR == point[0] and posC == point[1]:
                points.remove(point)
        #aggiunge un punto alla lista
        points.append((posR,posC,colors[index]))

    #controllo del tasto premuto

    if is_pressed("W"):
        posR += -1 if posR-1 > 1 else 0
    if is_pressed("A"):
        posC += -1 if posC-1 > 1 else 0
    if is_pressed("S"):
        posR += 1 if posR+1 < row else 0
    if is_pressed("D"):
        posC += 1 if posC+1 < col else 0

    #pulizia della trail del cursore
    with sc.location(old_posR,old_posC):
        print(" ")

    #cambia colore
    if is_pressed("c"):
        time.sleep(0.2)
        index += 1 if index<6 else -6
        with sc.location(0,0):
            print("SELECTED COLOR: ",end="")
            cprint("██",colors[index],end="")

    #disegna i punti salvati
    for point in points:
        with sc.location(point[0],point[1]):
            cprint("█",point[2])

    #disegna il cursore
    with sc.location(posR,posC):
        print("█")

    #salvataggio delle vecchie posizioni del cursore
    old_posR = posR
    old_posC = posC

    #delay
    if(is_pressed("f")):
        time.sleep(0.2)
    else:
        time.sleep(0.0001)
print("\u001b[2J")#fine programma