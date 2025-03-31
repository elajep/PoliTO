def trovaAdiacenti(mappa,riga,colonna):
    adiacenti = []
    for i in [riga-1,riga,riga+1]:
        if i >= 0 and i < len(mappa):
            for j in [colonna-1,colonna,colonna+1]:
                if j >= 0 and j < len(mappa[0]):
                    if (riga,colonna) != (i,j): adiacenti.append(mappa[i][j])
    adiacenti.sort(reverse=True)
    return adiacenti




media = []
mappa = []
infile = open('mappa.txt','r')
for line in infile:
    line = line.strip().split(' ')
    for i in range(len(line)):
        line[i] = int(line[i])
    mappa.append(line)

for i in range(len(mappa)):
    for j in range(len(mappa[0])):
        adiacenti = trovaAdiacenti(mappa,i,j)
        if adiacenti[0] < mappa[i][j]:
            media.append(mappa[i][j])
            print(f'{mappa[i][j]} {i} {j}')
print(f'la media è: {sum(media)/len(media)}m')
