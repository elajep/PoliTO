def main():
    originali = {}
    acquisti = {}

    infile = open('prodotti.txt','r')
    for line in infile:
        line = line.strip().split(' ')
        originali[line[0]] = [line[1]]
    infile.close()

    infile = open('acquisti.txt','r')
    for line in infile:
        line = line.strip().split(' ')
        if line[0] in acquisti:
            acquisti[line[0]].append(line[1])
        else: acquisti[line[0]] = [line[1]]
    infile.close()

    print('Elenco transazioni sospette: ')
    for prodotto in acquisti:
        if acquisti[prodotto] != originali[prodotto]:
            print(f'Codice prodotto: {prodotto}')
            print(f'Rivenditore ufficiale: {originali[prodotto][0]}')
            print(f'Lista rivenditori:',end='')
            for rivenditori in acquisti[prodotto]:
                print(f' {rivenditori}',end='')
            print()
            print()
main()
