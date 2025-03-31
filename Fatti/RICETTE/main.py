def main():
    costo = 0.0
    calorie = 0.0
    cibi = {}
    ricetta = {}
    avanti = True
    
    infile = open('cibi.txt','r')
    for line in infile:
        line = line.strip().split(';')
        line[0] = line[0].strip('\ufeff')
        cibi[line[0]] = [float(line[1]),float(line[2])]
    infile.close()

    file_da_aprire = input('INSERIRE NOME RICETTA: ')
    try: infile = open(file_da_aprire,'r')
    except:
        print('ERRORE APERTURA DEL FILE')
        exit

    riga = infile.readline()
    for line in infile:
        if line == '\n': 
            avanti = False
        if avanti:
            line = line.strip().split(';')
            ricetta[line[0]] = line[1]
            ricetta[line[0]] = int(ricetta[line[0]])
            costo += (ricetta[line[0]]/1000) * cibi[line[0]][0]
            calorie += (ricetta[line[0]]/1000) * cibi[line[0]][1]
    infile.close()

    print('Ingredienti:')
    for line in ricetta:
        print(f'{line} - {float(ricetta[line]):.1f}')
    print()
    print(f'Numero di ingredienti: {len(ricetta)}')
    print(f'Costo ricetta: {costo:.2f}')
    print(f'Calorie ricetta: {calorie:.2f}')

main()