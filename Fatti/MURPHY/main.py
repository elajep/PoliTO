def main():
    parole_lista = []
    leggi = {}
    infile = open('argomenti.txt','r') #metto in una lista le parole da cercare
    for parole in infile:
        parole_lista.append(parole.lower())
    infile.close()

    #creo un dizionario del tipo leggi = {'titolo':'spiegazione'}
    infile = open('leggi_di_Murphy.txt','r')
    lista = []
    for line in infile:
        if line != '\n':
            line = line.strip('\n') # creo una lista del tipo ['titolo','spiegazione']
            if len(lista) < 2:
                lista.append(line) #se non esiste lista[0] e lista[1] eseguo un append delle righe lette dal file
            else:
                lista[1] = f'{lista[1]} {line}' # se esiste gia lista[1] (spiegazione) aggiungile la riga successiva
            if len(lista) == 2 : leggi[lista[0]] = lista[1]
        else : lista = [] # quando incontro uno spazio cancello lista per creare una nuova chiave e un nuovo valore dizionario
    infile.close()

    gia_dette = [] # lista delle chiavi gia usate (da non ripetere)
    for parola in parole_lista:
        for chiavi in leggi:  # per ogni parola in argomenti.txt si leggono tutte le chiavi
            da_trovare = f'{chiavi} {leggi[chiavi]}' # si crea stringhe per cercare corrispondenza
            da_trovare = da_trovare.split() # si crea lista
            for i in range(len(da_trovare)): 
                da_trovare[i] = da_trovare[i].strip(" .,-\n").lower()

            if parola in da_trovare and chiavi not in gia_dette: #se si trova corrispondenza e chiave non ancora usata
                print (f'{chiavi} - ',end='') # si stampa il titolo
                if len(leggi[chiavi]) <= 50: # se la citazione è < 50 caratteri si stampa per intero
                    print(f' {leggi[chiavi]}')
                else:
                    for i in range(50): # altrim,enti si stampano solo i primi caratteri
                        print(leggi[chiavi][i],end='')
                    print('...')
                    gia_dette.append(chiavi)

main()
