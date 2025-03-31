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
    menu = {}
    infile = open('menu.txt','r')
    for line in infile:
        line = line.strip().split(', ')
        for i in [2,3] : line[i] = float(line[i])
        menu[line[0]] = line[1:]
    infile.close()

    ordine = []
    totale = 0.0
    iva_totale = 0.0
    print('RICEVUTA')
    infile = open('ordine.txt','r')
    for line in infile:
        line = line.strip().split(', ')
        ordine.append([line[1],menu[line[0]][0],menu[line[0]][1],menu[line[0]][2]])
        totale += float(line[1]) * menu[line[0]][1]
        iva_totale += float(line[1]) * (menu[line[0]][1]*(menu[line[0]][2]/100))
    infile.close()

    ordine.sort(key=itemgetter(3))
    for cibo in ordine:
        print(f' {cibo[0]} {cibo[1]:25}{cibo[2]:5.2f} {'IVA'}{cibo[3]:6.2f}%')
    print()
    print(f'Totale: {totale}€')
    print(f'Di cui IVA: {iva_totale:0.2f}€')

main()
