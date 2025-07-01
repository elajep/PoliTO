mazzo = []
infile = open('mazzo.txt','r')
for line in infile:
    mazzo.append(line.strip())
print()


for estrazione in range(int(len(mazzo)/5)):
    print(f'[ESTRAZIONE {estrazione+1}]:')
    mazzo_estratto = []
    for carta in range(5):
        mazzo_estratto.append(mazzo[(estrazione*5)+carta])
        print(f'    {mazzo[(estrazione*5)+carta]}',end='')
    print()
    print()

print()