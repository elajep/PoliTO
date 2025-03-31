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

personaggi = {}
infile = open('personaggi.txt','r')
for line in infile:
    line = line.strip().lower()
    personaggi[line] = 0
print()
infile.close()

cmd = input('Inserisci nome file: ')
infile = open(cmd,'r')
outfile = open('personaggi_altri.txt','a')
for line in infile:
    line = line.strip().split()
    for parola in line:
        parola = parola.strip("'.,-:;!?").lower()
        if parola in personaggi:
            personaggi[parola] += 1
infile.close()
nomi = sorted(personaggi)

min = nomi[0]
max = nomi[0]
for persone in nomi:
    if personaggi[persone] != 0: 
        print(f'{persone.upper()}: {personaggi[persone]} occorrenze')
        if personaggi[persone] > personaggi[max]: max = persone
        if personaggi[persone] < personaggi[max]: min = persone
    else:
        outfile.write(f'{persone.upper()}\n')
    
print(f'Il personaggio più ricorrente è {max.upper()}, quello meno ricorrente è {min.upper()}')
