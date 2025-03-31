def printPersone(personaggi):
    for persone in personaggi:
        print(f'{persone['nome']} - Sesso: {persone['sesso']}, Colore capelli:{persone['colore capelli']}, Lunghezza capelli:{persone['lunghezza capelli']}',end='')
        for chiavi in ['occhiali','cappello','baffi','barba','pelato']:
            if persone[chiavi] == 'si':
                print(f', {chiavi}',end='')
        print()
    print()

personaggi = []
domande = {}
infile = open('personaggi.txt','r')
linea = infile.readline()
linea = linea.strip().split(';')
for line in infile:
    line = line.strip().split(';')
    dizionario = {}
    for i in range(len(line)):
        dizionario[linea[i].lower()] = line[i].lower()
    personaggi.append(dizionario)
infile.close()

infile = open('domande2.txt','r')
for line in infile:
    line = line.strip().split('=')
    domande[line[0].lower()] = line[1].lower()
infile.close()

print('Persone nel gioco:')
printPersone(personaggi)

for pos,domanda in enumerate(domande):
    print()
    print(f'Mossa {pos+1} - domanda: {domanda} = {domande[domanda]}')
    print('Personaggi selezionati:')
    u = 0
    for i in range(len(personaggi)):
        if personaggi[u][domanda] != domande[domanda]:
            personaggi.pop(u)
        else : u += 1
    printPersone(personaggi)
print()
    
if len(personaggi) == 1:
    print("Gioco terminato, hai vinto! E' stato selezionato:")
    printPersone(personaggi)
else:
    print('Peccato, hai perso :-(')