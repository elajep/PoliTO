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

# [persone, animali, piante]

def main():
    from operator import itemgetter
    nazioni_list = []
    nazioni = {}
    infile = open('population.txt','r')
    for line in infile:
        line = line.strip().split(';')
        nazioni[line[0]] = [int(line[1])]
    infile.close()

    infile = open('animal_plant_count.txt','r')
    for line in infile:
        line = line.strip().split(';')
        nazioni[line[0]].append(int(line[1]))
        nazioni[line[0]].append(int(line[2]))
    infile.close()

    # [nome, d.animali, d.piante, green]
    for stati in nazioni: 
        densita_animali = nazioni[stati][1] / nazioni[stati][0]
        densita_piante = nazioni[stati][2] / nazioni[stati][0]
        green = ((densita_animali + densita_piante)/2) * 100
        nazioni_list.append([stati,round(densita_animali,4),round(densita_piante,4),round(green,2)])

    nazioni_list.sort(key=itemgetter(1),reverse=True)
    print(f'La nazione con il più alto rapporto di animali per popolazione è {nazioni_list[0][0]} con un rapporto di {nazioni_list[0][1]}.')
    nazioni_list.sort(key=itemgetter(2),reverse=True)
    print(f'La nazione con il più alto rapporto di piante per popolazione è {nazioni_list[0][0]} con un rapporto di {nazioni_list[0][1]}.')
    nazioni_list.sort(key=itemgetter(3),reverse=True)
    print('Le prime 3 nazioni in ordine decrescente di Indice Green sono:')
    for i in range(3):
        print(f'{i+1}. {nazioni_list[i][0]} - Indice Green: {nazioni_list[i][3]}')

main()

