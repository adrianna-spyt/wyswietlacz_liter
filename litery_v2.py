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
ekranname=pg.display.set_caption("Wyświetlacz liter")
pg.display.flip()
ekran.fill((0,0,0))
font = pg.font.SysFont("Arial",150)
ileliter=0
zacznij_od=0
czas_poczatkowy=time.time()
licznik=pg.time.get_ticks()
clock = pg.time.Clock()
timer_event = pg.USEREVENT+1
pg.time.set_timer(timer_event, 1000)
stan="litery"
indeks=0
indeksm=0
with open("litery_czas.txt", "a") as myfile:
    myfile.write("Początkowy czas:" + str(time.time()) + '\n')
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        elif event.type == timer_event:
            if ileliter>=10:
                stan="przerwa"
            if stan=="litery":
                font = pg.font.SysFont("Arial",150)
                poczatek_wyswietlania=time.time()
                with open("litery_czas.txt", "a") as myfile:
                    myfile.write(lista_liter[indeks] + ', ' + str(poczatek_wyswietlania) + '\n')
                aktualna_litera = font.render(lista_liter[indeks],True, (255,255,255))
                ekran.fill((0,0,0))
                ekran.blit(aktualna_litera,(410,220))
                pg.display.update()
                ileliter+=1
                if indeks==34:
                    indeks=0
                else:
                    indeks+=1
            if stan=="przerwa":
                poczatek_mrugania=time.time()
                font = pg.font.SysFont("Arial",70)
                with open("litery_czas.txt", "a") as myfile:
                    myfile.write('Czas na mruganie, ' + str(poczatek_mrugania) + '\n')
                ekran.fill((0,0,0))
                tekst=font.render("TERAZ MRUGAJ DOWOLNIE",True, (255,255,255))
                ekran.blit(tekst,(60,150))
                odliczanie=font.render(str(czas_mrugania[indeksm]),True,(255,255,255))
                ekran.blit(odliczanie,(430,250))
                pg.display.update()
                if indeksm==4:
                    stan="litery"
                    indeksm=0
                else:
                    indeksm+=1
                ileliter=0

pg.quit()
