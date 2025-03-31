def main():
    from operator import itemgetter
    agenda = {}
    infile = open('agenda.txt','r')
    for line in infile:
        line = line.strip().split(';')
        agenda[(line[0],line[1])] = line[2]
    print()
    infile.close()

    infile = open('comandi.txt','r')
    for line in infile:
        line = line.strip().split(' ',3)
        if line[0] == 'v':
            mostro = []
            for app in agenda:
                if app[0] == line[1]:
                    mostro.append(app)
            mostro.sort(key=itemgetter(1))
            for key in mostro:
                print(f'giorno {key[0]} ore {key[1]}: {agenda[key]}')
        elif line[0] == 'i':
            if (line[1],line[2]) not in agenda:
                agenda[(line[1],line[2])] = line[3]
                print('Appuntamento inserito correttamente')
                print(f'giorno {line[1]} ore {line[2]}: {line[3]}')
            else : print('Impossibile inserire appuntamento')
        else: print('Comando non riconosciuto')
    infile.close()

main()
