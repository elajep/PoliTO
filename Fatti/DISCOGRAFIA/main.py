# anni = {anno:[(codice1,tilolo1),(codice2,tilolo2),...]}
def main():
    anni = {}
    file_artisiti = []
    # creo la lista file_artisti = [(codice1,file1),(codice2,file2),...]
    infile = open('artisti.txt','r')
    for line in infile:
        line = line.strip().split(';')
        file_artisiti.append((line[0],line[1]))
    infile.close()
    
    # per ogni tupla in file_artisti
    # si apre il file corrispondente
        #legge ogni riga del file 'cantante'.txt
        # se l'anno è gia presente come chiave del dizionario anni
            # appende alla lista corrispondente alla chiave anno, la tupla (codice,tilolo)
        # se l'anno non è presente come chiave:
            # crea una lista che contiene la tupla (codice,titolo) con la chiave anno
    # creo una lista ordinata delle chiavi del dizionario anni

    for artista in file_artisiti: 
        codice = artista[0]
        fileDaAprire = artista[1]
        infile = open(fileDaAprire,'r')
        for line in infile:
            line = line.strip().split(';')
            anno = int(line[0])
            titolo = line[1]
            if anno in anni:
                anni[anno].append((codice,titolo))
            else:
                anni[anno] = [((codice,titolo))]
        infile.close()
    lista_anni = sorted(list(anni))


    # per ogni anno nella lista
        # visualizzo l'anno
        # cerco la lista corrispontente all'anno nel dizionario
        # per ogni elemento della lista visualizzo titolo e codice artista
        
    for anno in lista_anni:
        print(f'{anno}:')
        for canzone in anni[anno]:
            print(f'{canzone[1]:32}{canzone[0]}')
main()