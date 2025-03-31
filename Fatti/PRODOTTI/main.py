from operator import itemgetter
essenziali = set()
shops = {}

with open('shops.txt', 'r') as infile_shop:
    for line in infile_shop:
        line = line.strip()
        shops[line] = {} 

with open('NLFoodPricing.csv', 'r') as infile_food:

    infile_food.readline()
    
    for line in infile_food:
        line = line.strip().split(',')

        if line[4] == 'E':
            essenziali.add(line[3])

            if line[2] in shops:
                prodotto = line[3]
                prezzo = float(line[5])

                if prodotto not in shops[line[2]] or shops[line[2]][prodotto] > prezzo:
                    shops[line[2]][prodotto] = prezzo


essenziali_list = sorted(list(essenziali))
shops_list = sorted(list(shops))
print('Prodotti:')
for prodotto in essenziali_list:
    print(f'- {prodotto}')


for negozio in shops_list:
    scaffale = []
    for prodotti in list(shops[negozio]):
        scaffale.append([prodotti,shops[negozio][prodotti]])
    scaffale.sort()
    print()
    print(f'{negozio}:')
    for prodotti in scaffale:
        print(f'- {prodotti[0]}: {prodotti[1]:0.2f} $/chilo')
print()

cmd = input('Che cibo vuoi cercare? (q per smettere): ')
while cmd != 'q':
    prodotto = []
    for negozi in shops:
        if cmd in shops[negozi]:
            prodotto.append([negozi,shops[negozi][cmd]])
    if prodotto != []:
        prodotto.sort(key=itemgetter(1))
        print(f'Prezzo minimo: {prodotto[0][1]} $/chilo da {prodotto[0][0]}')
    else:
        print('Prodotto non disponibile')
    print()
    cmd = input('Che cibo vuoi cercare? (q per smettere): ')
print('Arrivederci')