from operator import itemgetter

def main():
    lista_punti = []
    zodiacoDate = {} # { (giorno_iniz,mese_iniz) , (giorno_fin,mese_fin) , punti }
    infile = open('zodiaco.csv','r')
    for line in infile:
        line = line.strip().split(',')
        line[1] = line[1].split('/')
        line[2] = line[2].split('/')
        zodiacoDate[line[0]] = [(int(line[1][0]),int(line[1][1])),(int(line[2][0]),int(line[2][1])),0]
    infile.close()

    infile = open('sportivi.csv','r')
    for line in infile:
        line = line.strip().split(',')
        data = line[-1].split('/')
        giorno = int(data[0])
        mese = int(data[1])
        punti = int(line[1])

        for segni in zodiacoDate:
            date = zodiacoDate[segni]
            if (mese == date[0][1] and giorno >= date[0][0]) or (mese == date[1][1] and giorno <= date[1][0]):
                zodiacoDate[segni][2] += punti
    infile.close()

    for segni in zodiacoDate:
        lista_punti.append([segni,zodiacoDate[segni][2]])
    lista_punti.sort(key=itemgetter(1),reverse=True)

    max_punteggio = lista_punti[0][1]
    for coppie in lista_punti:
        print(f'{coppie[0]:11}({coppie[1]})',end=' ')
        print('*' * int((coppie[1]*50)/max_punteggio))
main()
