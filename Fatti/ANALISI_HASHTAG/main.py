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
giorni = {}
infile = open('hashtags.csv','r')
for line in infile:
    line = line.strip().split(' ')
    if line[0][-1] not in giorni : giorni[line[0][-1]] = {}
    for elementi in line:
        if elementi[0] == '#':
            if elementi not in giorni[line[0][-1]]:
                giorni[line[0][-1]][elementi] = 1
            else: giorni[line[0][-1]][elementi] += 1


giorni_list = list(giorni)
hasht = list(giorni[giorni_list[0]])

print('Hashtag in tendenza:')
for hashtag in hasht:
    g1 = giorni[giorni_list[0]]
    g2 = giorni[giorni_list[1]]
    if  hashtag in g1 and hashtag in g2:
        if ((g2[hashtag] - g1[hashtag])/g1[hashtag])*100 >= 50:
            print(f'{hashtag} con un incremento del {round(((g2[hashtag] - g1[hashtag])/g1[hashtag])*100)}%')
    
