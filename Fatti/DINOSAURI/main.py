from time import * 
# importi le variabili
start = time()
giocatori = [[],[]]
punti = [0,0]
tavolo = 0

# lettura del file
infile = open('mazzo.txt','r')
# per ogni riga
for pos, line in enumerate(infile):
    line = line.strip()
    # voglio line = ('Colore', valore)
    if line == 'Rosso': line = ('Rosso', 5)
    elif line == 'Verde': line = ('Verde', 3)
    elif line == 'Giallo': line = ('Giallo', 1)

    # se la posizione della carta è pari, la carta è del giocatore 1 altrimenti è del giocatore 2
    if pos%2 == 0:
        giocatori[0].append(line)
    else: giocatori[1].append(line)
infile.close() # chiudo il file

# mostro i punteggi iniziali
for id in range(len(punti)):
    print(f'Punteggio giocatore {id+1}: {punti[id]}')

#gioco le mani
for manche in range(len(giocatori[0])):

    # mostro il numero della mano
    print()
    print(f'Mano n. {manche+1}')

    for id in [0,1]:
        print(f'Carta giocatore {id+1}: {giocatori[id][manche][0]}') # mostro carte mano

    # se le carte estratte sono uguali aggiungi le due carte al punteggio del tavolo
    if giocatori[0][manche][1] == giocatori[1][manche][1]:
        tavolo += (giocatori[0][manche][1])*2 # dato che le carte sono uguali aggingo carta * 2

    # se le carte non sono uguali controllo chi è il vincitore
    else:
        if  giocatori[0][manche][1] > giocatori[1][manche][1] : winner_index = 0
        else: winner_index = 1
        # aggiungo i punti del tavolo + la somma delle due carte estratte al vincitore
        punti[winner_index] += giocatori[1][manche][1] + giocatori[0][manche][1] + tavolo
        # pulisco il tavolo
        tavolo = 0

    # mostro i punteggi dei giocatori
    for id in [0,1]:
        print(f'Punteggio giocatore {id+1}: {punti[id]}')
print()

# alla fine delle mani controllo il vincitore e mostro il risultato
if punti[0] != punti[1]:
    print(f'Vince il giocatore {punti.index(max(punti))+1} con {max(punti)} punti.')
else: print('Il gioco finisce con un pareggio')
end = time()

print(end-start)