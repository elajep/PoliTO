from operator import itemgetter
indicatori = []
città = []
infile = open('indicatore.txt','r')
indicatore = infile.readline().strip()
print(indicatore)
infile.close()

infile = open('20201214_QDV2020_001.csv','r')
riga = infile.readline()
for line in infile:
    line = line.strip().split(',')
    if line[5] not in indicatori:
        indicatori.append(line[5])
    if line[5] == indicatore:
        città.append((line[3],float(line[4])))
print()
città.sort(key=itemgetter(1),reverse=True)

print('Indicatori della qualità della vita:')
for elemento in indicatori:
    print(elemento)
print()
print(f"Classifica secondo l'indicatore '{indicatore}':")
for elemento in città:
    print(f'{elemento[0]:23}:{elemento[1]:8.3f}')
