def main():
    giocatori = {}

    infile = open('risultati_gara.txt','r')
    for line in infile:
        line = line.strip().split(';')
        giocatori[line[-1]] = line[:5]
        giocatori[line[-1]][4] = int(giocatori[line[-1]][4])
        if giocatori[line[-1]][4] % 10 != 0:
            minuti = int(giocatori[line[-1]][4]/10)
            secondi = round((giocatori[line[-1]][4]/10 - minuti) * 0.6,2)
            giocatori[line[-1]][4] = minuti + secondi
        else: giocatori[line[-1]][4] = giocatori[line[-1]][4]/10
    infile.close()

    infile = open('database_atleti.txt','r')
    for line in infile:
        line = line.strip().split(';')
        giocatori[line[0]].append(float(line[1]))
    infile.close()

    print('CLASSIFICA DEI PARTECIPANTI:')
    for categoria in ['M','F']:
        print()
        print(f'Categoria: {categoria}')
        for id in giocatori:
            if giocatori[id][3] == categoria:
                print(f'{giocatori[id][0]} {giocatori[id][1]}, {giocatori[id][4]} min/Km')
    print()
    print('ATLETI CHE HANNO SUPERATO IL RECORD PERSONALE')
    print()
    for id in giocatori:
        if giocatori[id][4] < giocatori[id][5]:
            print(f'{giocatori[id][0]} {giocatori[id][1]}')
    print()
main()