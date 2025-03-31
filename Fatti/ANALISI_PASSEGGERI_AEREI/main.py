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
voli = {}
origini = {}
infile = open('passeggeri.txt','r')
indice = infile.readline()
for line in infile:
    line = line.strip().split(',')

    if line[-1] not in voli:
        if line[2] == 'M': voli[line[-1]] = [1,0,1]
        elif line[2] == 'F': voli[line[-1]] = [0,1,1]
    else:
        voli[line[-1]][2] += 1
        if line[1] == 'M': 
            voli[line[-1]][0] += 1
        
        else:
            voli[line[-1]][1] += 1

    if line[3] not in origini:
        origini[line[3]] = [int(line[1])]
    else: origini[line[3]].append(int(line[1]))

print("Media dell'età per ciascuna origine")
for origine in origini:
    print(f'Origine: {origine}, Media età: {round(sum(origini[origine])/len(origini[origine]),1)}')
print()

key = list(voli)
max = key[0]
for numero in key:
    if voli[numero][2] > voli[max][2]:
        max = numero
print(f'Numero di volo più popolare: {max}, Passeggeri M: {voli[max][0]} / F: {voli[max][1]}')