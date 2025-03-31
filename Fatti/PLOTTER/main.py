tabella = []
for col in range(20):
    riga = [' ']*20
    tabella.append(riga)
print()

infile = open('plotter.txt','r')
for line in infile:
    line = line.strip().split(' ')
    
    for valore in range(1,len(line)):
        line[valore] = int(line[valore])
    print()

    if line[0] == 'P':
        tabella[line[2]][line[1]] = '*'

    elif line[0] == 'H':
        for i in range(line[3]):
          if tabella[line[2]][line[1]+i] == ' ':
              tabella[line[2]][line[1]+i] = '-'
          elif tabella[line[2]][line[1]+i] == '|':
              tabella[line[2]][line[1]+i] = '+'
    
    elif line[0] == 'V':
        for i in range(line[3]):
          if tabella[line[2]+i][line[1]] == ' ':
            tabella[line[2]+i][line[1]] = '|'
          elif tabella[line[2]+i][line[1]] == '-':
              tabella[line[2]+i][line[1]] = '+'
    else : print('COMANDO NON RICONOSCIUTO')
infile.close()

for row in range(len(tabella)):
    for colonna in range(len(tabella[0])):
        print(tabella[row][colonna],end=' ')
    print()

