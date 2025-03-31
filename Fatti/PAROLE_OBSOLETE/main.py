parole = {}
conteggio = 0
outfile = open('nuovotesto.txt','w')
infile = open('obsoleto.txt','r')
for line in infile:
    line = line.split(' ')
    for elementi in range(len(line)):
        line[elementi] = line[elementi].strip().strip('\ufeff')
    parole[line[0]] = [line[1],0]
infile.close()

infile = open('testo.txt','r',encoding='utf-8')
for line in infile:
    line = line.split(' ')
    for elementi in line:
        if elementi != '\n' : conteggio += 1
        if elementi in parole:
            outfile.write(parole[elementi][0])
            parole[elementi][1] += 1
        else: outfile.write(f'{elementi} ')

print(f'Il numero di parole presenti nel testo è: {conteggio}')
print('Le parole obsolete sono così riportate nel testo originale:')
for parola in parole:
    print(f'{parola}: {parole[parola][1]}')