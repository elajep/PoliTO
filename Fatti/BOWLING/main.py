# lista = {(nome,cognome):[totale,volte_10,volte_0]}
import time
from operator import itemgetter
start = time.time()
def main():
    giocatori = []
    lista_totale = []
    infile = open('bowling.txt','r')
    for line in infile:
        line = line.strip()
        line = line.split(';')
        dati_giocatore = (line[0], line[1])
        line.pop(0)
        line.pop(0)
        totale = 0
        volte_10 = 0
        volte_0 = 0
        for numero in line:
            totale += int(numero)
            if numero == '10' : volte_10 += 1
            if numero == '0' : volte_0 += 1
        lista_totale.append(totale)
        lista_totale.sort(reverse=True)
        giocatori.append({'dati':dati_giocatore,'totale':totale,'volte_10':volte_10,'volte_0':volte_0})
    giocatori.sort(key=itemgetter('totale'),reverse=True)
    for giocatore in giocatori:
        print(f'{giocatore['dati'][0]:11} {giocatore['dati'][1]:11} {giocatore['totale']}')

    giocatori.sort(key=itemgetter('volte_10'),reverse=True)
    if giocatori[0]['volte_10'] != 0:
        for giocatore in giocatori:
            if giocatore['volte_10'] == giocatori[0]['volte_10']:
             print(f'{giocatore['dati'][0]} {giocatore['dati'][1]} ha buttato giù tutti i birilli {giocatore['volte_10']} volta/e')
    
    giocatori.sort(key=itemgetter('volte_0'),reverse=True)
    if giocatori[0]['volte_0'] != 0:
        for giocatore in giocatori:
            if giocatore['volte_0'] == giocatori[0]['volte_0']:
                print(f'{giocatore['dati'][0]} {giocatore['dati'][1]} non ha buttato più nessun birillo {giocatore['volte_0']} volta/e')
    infile.close()
main()
stop = time.time()
print(stop-start)