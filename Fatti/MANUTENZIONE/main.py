def main():
    from operator import itemgetter
    aop = {'a':[], 'p':[]}
    def listaData (stringa):
        stringa = stringa.split('/')
        for i in range(len(stringa)) : stringa[i] = int(stringa[i])
        stringa = stringa[::-1]
        return stringa

    infile = open('parametri.txt','r')
    parametri = infile.readline().strip().split(',')
    infile.close()
    data_ricerca = listaData(parametri[0])

    infile = open('manutenzione.txt','r')
    for line in infile:
        line = line.strip().split(',')
        line[2] = int(line[2])
        costo = line[2]
        data = listaData(line[1])

        if data > data_ricerca:
                aop['p'].append(line)
        else:
            aop['a'].append(line)
    print()
        
    print ('le operazioni ',end='')
    if parametri[1] == 'a': print('effettuate prima del ',end='')
    else : print('da effettuare dopo il ' ,end='')
    print(f'{parametri[0]} sono:')
    print()
    ordinata = sorted(aop[parametri[1]],key=itemgetter(2),reverse=True)
    for elementi in aop[parametri[1]]:
        print(f'  {elementi[0]} in data {elementi[1]} costo {elementi[2]} euro')

    print()
    if parametri[1] == 'a': print(f'La manutenzione più costosa è stata {ordinata[0][0]} del ',end='')
    else : print(f'La manutenzione più costosa da effetuare è {ordinata[0][0]} in data ' ,end='')
    print(f'{ordinata[0][1]} costata {ordinata[0][2]} euro')

main()


