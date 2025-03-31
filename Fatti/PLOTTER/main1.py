tabella=[]
for colonna in range (20):
    riga = [" "]*20
    tabella.append(riga)
print()
infile=open("plotter.txt","r")
for line in infile:
    line=line.strip().split(" ")
    for valore in range(1,len(line)):
        line[valore]=int(line[valore])


    if line[0]=="P":
        tabella[line[2]][line[1]]="*"

    elif line[0]=="H":
        for i in range (line[3]):
            if tabella[line[2]][line[1]+i]==" ":
                tabella[line[2]][line[1]+i]="-"
            if tabella[line[2]][line[1]+i]=="|":
                tabella[line[2]][line[1]+i]="+"
    
    elif line[0]=="V":
        for i in range (line[3]):
            if tabella[line[2]+i][line[1]]==" ":
                tabella[line[2]+i][line[1]]="|"
            if tabella[line[2]+i][line[1]]=="-":
                tabella[line[2]+i][line[1]]="+"
            
infile.close()

for row in range(len(tabella)):
    for colon in range(len(tabella[0])):
        print(tabella[19-row][colon],end=" ")
    print()