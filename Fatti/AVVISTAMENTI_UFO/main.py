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

from operator import itemgetter
tempo = {}
paesi = {}
infile = open('ufo_sightings.csv','r')
for line in infile:
    line = line.strip().split(',')
    if line[2] in paesi : paesi[line[2]] += 1
    else: paesi[line[2]] = 1
    tempo[int(line[4])] = [line[-1],line[3]]


maggiore = sorted(tempo,reverse=True)
print(f'Avvistamento di durata più lunga: {tempo[maggiore[0]][0]} (Durata: {maggiore[0]} secondi, Forma: {tempo[maggiore[0]][1]})')

lista_paesi = list(paesi)
max = lista_paesi[0]
for valori in paesi:
    if paesi[valori] > paesi[max] : max = valori

print(f'Paese con il maggior numero di avvistamenti: {max}')




