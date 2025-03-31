def trovaAdiacenti(mappa,riga,colonna):
    adiacenti = []
    for r in [riga-1,riga,riga+1]:
        if 0 <= r < len(mappa):
            for c in [colonna-1,colonna,colonna+1]:
                if 0 <= c < len(mappa[r]):
                    if (r != riga) or (c != colonna):
                        adiacenti.append(mappa[r][c])
    return adiacenti

def verificoCima(adiacenti,i,j,mappa):
    cima = True
    adiacenti.sort(reverse=True)
    if adiacenti[0] >= mappa[i][j] : cima = False
    return cima

lista_cimeVal = []
mappa = []
infile = open('mappa.txt','r')
for line in infile:
    line = line.strip()
    line = line.split(' ')
    lista_numeri = []
    for numeri in line:
      lista_numeri.append(int(numeri))


    mappa.append(lista_numeri)
infile.close()

for i in range(len(mappa)):
    for j in range(len(mappa[0])):
        adiacenti = trovaAdiacenti(mappa,i,j)

        if verificoCima(adiacenti,i,j,mappa):
            print (f'{mappa[i][j]} {i} {j}')
            lista_cimeVal.append(mappa[i][j])
print(f'media cime {sum(lista_cimeVal)/len(lista_cimeVal)} m')