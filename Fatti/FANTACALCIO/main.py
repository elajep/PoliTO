from operator import itemgetter
budget_e_composizione = {'centrocampista':(80,8),'difensore':(40,8),'attaccante':(120,6),'portiere':(20,3)}
giocatori = {}

infile = open('fantacalcio.txt','r')
for line in infile:
    line = line.strip().split(',')
    valore = int(line[-1])
    ruolo = line[-2][1:]
    nome = line[0]
    if ruolo in giocatori:
        giocatori[ruolo].append((nome,valore))
    else: giocatori[ruolo] = [(nome,valore)]
infile.close()

for ruolo in giocatori:

    print (f'{ruolo[:-1].capitalize()}i: ',end='')

    pull = sorted(giocatori[ruolo],key=itemgetter(1),reverse=True)
    posti = budget_e_composizione[ruolo][1]
    budget_totale = budget_e_composizione[ruolo][0]

    for giocatore in range(posti):
        trovato = False
        budget_giocatore = budget_totale - (posti-giocatore-1)
        
        i = 0
        while not trovato:
            if pull[i][1] <= budget_giocatore:
                print(f'{pull[i][0]} {pull[i][1]}',end= ' ')
                budget_totale -= pull[i][1]
                pull.pop(i)
                trovato = True
            else: i += 1
    print()