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


def main():
    from operator import itemgetter
    media = []
    tot_passeggeri = 0
    luoghi = {}
    pietre = {}

    infile = open('viaggi_nemo.txt','r')
    for line in infile:
        line = line.strip().split(',')
        media.append(int(line[1]))
        tot_passeggeri += int(line[2])
        luoghi[line[0]] = set()
    infile.close()

    infile = open('pietre_preziose_luoghi.txt','r')
    for line in infile:
        line = line.strip().split(',')
        if line[0] in luoghi:
            for i in range(1,len(line)) :
                luoghi[line[0]].add(line[i])
                if line[i] not in pietre: pietre[line[i]] = 0
    infile.close()

    for paesi in luoghi:
        for pietra in luoghi[paesi]:
            pietre[pietra] += 1

    pietre_lista = []

    for sasso in pietre:
        pietre_lista.append((sasso,pietre[sasso]))
    pietre_lista.sort(key=itemgetter(1),reverse=True)

    print(f'Durata media dei viaggi: {sum(media)/len(media):0.2f}')
    print(f'Numero totale di passeggeri: {tot_passeggeri}')
    print('Tipi di pietre preziose per luogo visitato:')
    for posti in luoghi:
        print(f'- {posti}: ',end='')
        for pietre in luoghi[posti]:
            print(f'{pietre}, ',end='')
        print()
    print('I tre tipi di pietre preziose più comuni: ',end='')
    for i in range(3):
        print(f'{pietre_lista[i][0]}, ',end='')

main()