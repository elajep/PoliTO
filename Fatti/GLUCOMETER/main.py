def main():
    from operator import itemgetter
    letture = {}
    superamento = {}
    superamento_ordinato = []
    infile = open('glucometers.txt','r')
    for line in infile:
        line = line.strip().split(' ')
        if line[0] in letture:
            letture[line[0]].append((line[1],line[2]))
        else: letture[line[0]] = [(line[1],line[2])]
        valore = line[2]
        if int(valore) >= 200:
            if line[0] in superamento:
                superamento[line[0]] += 1
            else: superamento[line[0]] = 1

    for chiavi in superamento:
        superamento_ordinato.append((chiavi,superamento[chiavi]))
    superamento_ordinato.sort(key=itemgetter(1),reverse=True)

    for tupla in superamento_ordinato:
        print()
        chiave = tupla[0]
        for valori in letture[chiave]:
            if int(valori[1]) >= 200:
                print(f'{chiave} {valori[0]} {valori[1]}')
main()