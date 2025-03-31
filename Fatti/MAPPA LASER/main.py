def printtab (lista):
    for i in range(len(lista)):
        for j in range(len(lista[0])):
            print(f'{lista[i][j]:2}',end=' ')
        print()

def trovoAdiacenti(mappa,D,y,x):
    raggio = D+1
    adiacenti = []
    for i in range(y-raggio,y+raggio):
        if i >= 0 and i <= len(mappa)-1:
            for j in range(x-raggio,x+raggio):
                if j >= 0 and j <= len(mappa[0])-1:
                    if (i,j) != (y,x) : adiacenti.append(mappa[i][j])
    adiacenti.sort(reverse=True)
    return adiacenti

def main():
    D = 2
    mappa = []
    mappaDaStampare = []
    infile = open('mappa.txt','r')
    for line in infile:
        line = line.strip().split(' ')
        for i in range(len(line)) : line[i] = int(line[i])
        mappa.append(line)
        mappaDaStampare.append(['-']*len(mappa[0]))

    for i in range(len(mappa)):
        for j in range(len(mappa[0])):
            adiacenti = trovoAdiacenti(mappa,D,i,j)
            if mappa[i][j] > adiacenti[0] : mappaDaStampare[i][j] = mappa[i][j]
    printtab(mappaDaStampare)

main()