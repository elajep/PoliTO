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

def printab(lista):
    for i in range(len(lista)):
        for j in range(len(lista[0])):
            if lista[i][j] <= 0 : print('_',end='')
            else : print(lista[i][j],end='')
        print()
    print()


def main():
    mappa = []
    infile = open('mappa.txt','r')
    for line in infile:
        line = line.strip()
        linea = []
        for char in line : 
            if char == '_' : linea.append(0)
            else: linea.append(int(char))
        mappa.append(linea)

    printab(mappa)
    maxi = 0
    maxj = 0
    max_somma = 0
    for j in range(len(mappa[0])):
        somma = 0
        for i in range(len(mappa)): 
            somma += mappa[i][j]
            if sum(mappa[i]) > sum(mappa[maxi]) : maxi = i
        if somma > max_somma:
            max_somma = somma
            maxj = j
    coorinate = (maxi,maxj)
    print(f'Le cordinate del centro del ciclone sono {coorinate} valore: {mappa[maxi][maxj]}')

    u = 0

    printab(mappa)

    while u < 6:

        for i in range(len(mappa)):
            j = len(mappa[0])-1
            while mappa[i][j] == 0 or j == 0 :  j -= 1
            if mappa[i][j] > 0 : mappa[i][j] -= 1
            mappa[i].pop(-1)
            mappa[i].insert(0,0)
        u += 1
        printab(mappa)
main()


    
