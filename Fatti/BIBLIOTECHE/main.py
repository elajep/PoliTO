# Write your solution here, DO NOT START A NEW PROJECT
# ATTENTION: if you create a new project, your exam paper will not be collected
#            and you will be obliged to come in the subsequent exam session
#
# ATTENTION: on Win 10 (Italian keyboard) characters like [ ] { } have to be
#            created using ALTgr+è (e.g. for [ ) and NOT CTRL-ALT-è
#
# ATTENTION: on macOS you have to use CTRL-C and CTRL-V inside the virtual
#            machine and NOT command-C command-V
#
# if your keyboard is broken you can do copy/paste also with mouse
# and you can copy special characters like [ ] { } < > here
#
# Scrivete qui la vostra soluzione, NON CREATE UN NUOVO PROGETTO
# ATTENZIONE: se create un nuovo progetto il vostro compito non sara'
#             raccolto correttamente e dovrete tornare all'appello successivo
#
# ATTENZIONE: su Win 10 (tastiera italiana) i caratteri speciali (es. { ) vanno
#             scritti ad esempio con ALTgr+è (caso di [ ) e NON CTRL-ALT-è
#
# ATTENZIONE: su macOS vanno usati CRTL-C e CTRL-V per il copia incolla
#                       nella macchina virtuale e NON command-C command-V
#
# se la vostra tastiera è guasta potete fare copia/incolla anche con il mouse
# e per i caratteri speciali potete copiare da questi caratteri  [  ]  {  }  <  >
# print(string.punctuation)
## ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~

codici = {}
titoli = {}
regalo = 0
copie = 0

infile = open("inventarioOld.csv", "r")
for line in infile:
    line = line.strip().split(";")
    isbn = line[1]
    titolo = line[2]
    if isbn not in titoli: titoli[isbn] = [line[2],line[3].strip()]
    codiceCopia = line[0]
    if isbn not in codici:
        codici[isbn] = [codiceCopia]
    else:
        codici[isbn] += [codiceCopia]
infile.close()

fileNew = open('invertarioNew.csv','a')
fileScuola = open('inventarioScuola.csv','a')

for isbn in codici:
    if len(codici[isbn]) > 3:
        regalo += 1
        fileNew.write(f'{isbn};{titoli[isbn][1]};{titoli[isbn][0]}')

        for i in range(3):
            fileNew.write(f';{codici[isbn][0]}')
            codici[isbn].pop(0)
        fileNew.write('\n')
        fileScuola.write(f'{isbn};{titoli[isbn][1]};{titoli[isbn][0]}')
        
        for i in range(len(codici[isbn])):
            fileScuola.write(f';{codici[isbn][i]}')
            copie += 1
        fileScuola.write('\n')

    else:
        fileNew.write(f'{isbn};{titoli[isbn][1]};{titoli[isbn][0]}')
        for libro in codici[isbn]:
            fileNew.write(f';{libro}')
        fileNew.write('\n')
print(f'Numero libri da regalare: {regalo}, copie totali: {copie}')