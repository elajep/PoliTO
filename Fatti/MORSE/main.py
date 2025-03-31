morseToAlpha = {}
alphaToMorse = {}
comandi = []

infile = open('morse.txt','r')
for line in infile:
    line = line.strip()
    line = line.split(' ')
    morseToAlpha[line[1]] = line[0]
    alphaToMorse[line[0]] = line[1]
infile.close()

infile = open('comandi.txt','r')
for line in infile:
    line = line.strip()
    line = line.split(' ')
    comandi.append((line[0],line[1]))
infile.close()

for comando in comandi:
    infile = open(comando[1],'r')
    if comando[0] == 'c':
        print(f'Codifica del file {comando[1]}:')
        line = infile.readline()
        line = line.strip()
        for char in line:
            char = char.upper()
            if char in alphaToMorse:
                print(f'{alphaToMorse[char]} ',end='')
        print()
        
    if comando[0] == 'd':
        print(f'Decodifica del file {comando[1]}:')
        for line in infile:
            line = line.strip()
            line = line.split(' ')
            for char in line:
                if char in morseToAlpha:
                    print(morseToAlpha[char],end='')
            print()
    infile.close()