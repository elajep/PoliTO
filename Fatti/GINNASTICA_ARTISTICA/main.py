def main():
    from operator import itemgetter
    nazioni = {}
    nazioni_ordiante = []
    gara_femminile = []
    infile = open('punteggi.txt','r')
    for line in infile:
        line = line.strip().rsplit(' ',7)
        punteggi = line[3:]
        for i in range(len(punteggi)) : punteggi[i] = float(punteggi[i]) #trasformo str in float
        punteggi.sort()
        punteggi.pop(0)
        punteggi.pop(-1)
        somma = round(sum(punteggi),3)
        if line[2] in nazioni:
            nazioni[line[2]] += somma
        else: nazioni[line[2]] = somma
        if line[1] == 'F':
            gara_femminile.append([line[0],line[2],somma])
    infile.close()

    gara_femminile.sort(key=itemgetter(2),reverse=True)
    print('Vincitrice femminile:')
    print(f'{gara_femminile[0][0]}, {gara_femminile[0][1]} - Punteggio: {gara_femminile[0][2]}')
    print()

    for paesi in nazioni:
        nazioni_ordiante.append((paesi,nazioni[paesi]))
    nazioni_ordiante.sort(key=itemgetter(1),reverse=True)

    for posizione in range(3):
        print(f'{posizione+1}°) {nazioni_ordiante[posizione][0]} - Punteggio Finale: {nazioni_ordiante[posizione][1]}')
main()