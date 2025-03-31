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

def assegnaPunti(punti):
    if punti[0] == punti[1] : return [2,2]
    if punti[0] > punti[1]: return[3,1]
    elif punti[0] < punti[1]: return[1,3]

# [GIOCATE, PUNTI, PF, PS]
def main():
    from operator import itemgetter
    squadretot = {}
    squadra_lista = []
    infile = open('torneo.txt','r')
    for line in infile:
        line = line.strip().split(':')
        squadre = line[0].split('-')
        punti = line[1].split('-')
        for i in range(2):
            squadre[i] = squadre[i].strip()
            punti[i] = int(punti[i])
        

        punti_partita = assegnaPunti(punti)
        for i in range(len(squadre)):
            if squadre[i] not in squadretot: squadretot[squadre[i]] = [1,punti_partita[i],punti[i],punti[i-1]]
            else:
                for pos, pun in enumerate([1,punti_partita[i],punti[i],punti[i-1]]):
                    squadretot[squadre[i]][pos] += pun
    infile.close()

    for squadra in squadretot:
        q = round(squadretot[squadra][2]/squadretot[squadra][3],3)
        squadra_lista.append([squadra,squadretot[squadra][0],squadretot[squadra][1],squadretot[squadra][2],squadretot[squadra][3],q])

    squadra_lista.sort(key=itemgetter(2,5),reverse=True)
    print('SQUADRA              GIOCATE PUNTI       Q     PF    PS')
    print('-------------------------------------------------------')
    for squadra in squadra_lista:
        print(f'{squadra[0]:22}{squadra[1]}{squadra[2]:11}{squadra[5]:8}{squadra[3]:7}{squadra[4]:6}')

main()