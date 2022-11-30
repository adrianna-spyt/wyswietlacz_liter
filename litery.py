# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
import pygame as pg
import time

running=True
szerokosc_ekranu=900
wysokosc_ekranu=600
lista_liter=["A","Ą","B","C","Ć","D","E","Ę","F","G","H","I","J","K","L","Ł","M","N","Ń","O","Ó","P","Q","R","S","Ś","T","U","V","W","X","Y","Z","Ź","Ż"]
# lista_liter=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
czas_mrugania=[5,4,3,2,1]
pg.init()
ekran=pg.display.set_mode((szerokosc_ekranu,wysokosc_ekranu))
ekranname=pg.display.set_caption("Litery")
pg.display.flip()
ekran.fill((0,0,0))
font = pg.font.SysFont("Arial",150)
ileliter=0
zacznij_od=0
czas_poczatkowy=time.time()
with open("litery_czas.txt", "a") as myfile:
    myfile.write("Początkowy czas:" + str(time.time()) + '\n')
while running:
    # przycisk = pg.key.get_pressed()
    # if przycisk[pg.K_ESCAPE]:
    #     self.running=False
    #     break
    for i in range(zacznij_od,len(lista_liter)):
        poczatek_wyswietlania=time.time()
        with open("litery_czas.txt", "a") as myfile:
            myfile.write(lista_liter[i] + ', ' + str(poczatek_wyswietlania) + '\n')
        aktualna_litera = font.render(lista_liter[i],True, (255,255,255))
        ekran.fill((0,0,0))
        ekran.blit(aktualna_litera,(410,220))
        pg.display.update()
        ileliter+=1
        while time.time()<poczatek_wyswietlania+1:
            pass
        if i<len(lista_liter)-2:
            zacznij_od=i+1
        else:
            zacznij_od=0
        if ileliter>=10:
            break
    if ileliter>=10:
        poczatek_mrugania=time.time()
        font = pg.font.SysFont("Arial",70)
        with open("litery_czas.txt", "a") as myfile:
            myfile.write('Czas na mruganie, ' + str(poczatek_wyswietlania) + '\n')
        for j in range(len(czas_mrugania)):
            while time.time()<poczatek_mrugania+j+1:
                ekran.fill((0,0,0))
                tekst=font.render("TERAZ MRUGAJ DOWOLNIE",True, (255,255,255))
                ekran.blit(tekst,(60,150))
                odliczanie=font.render(str(czas_mrugania[j]),True,(255,255,255))
                ekran.blit(odliczanie,(430,250))
                pg.display.update()
        ileliter=0
        font = pg.font.SysFont("Arial",150)
