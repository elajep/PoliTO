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
    robot = {}
    robot_list = []
    max_severity = set()

    infile = open('allarmi.csv','r')
    indice = infile.readline()
    for line in infile:
        line = line.strip().split(';')
        if line[0] not in robot:
            robot[line[0]] = 1
        else: robot[line[0]] += 1
        max_severity.add((int(line[1]),line[0]))

    for key in robot:
        robot_list.append((robot[key],key))
    robot_list.sort(key=itemgetter(0),reverse=True)
    for valori in robot_list: print(f'Per il robot {valori[1]} si sono verificati {valori[0]} allarmi')

    max_severity = sorted(max_severity,reverse=True,key=itemgetter(0))
    print()
    print(f'Il livello massimo di severità {max_severity[0][0]} è stato raggiunto dai seguenti robot:')
    for error in max_severity:
        if error[0] == max_severity[0][0] : print(error[1])

main()



