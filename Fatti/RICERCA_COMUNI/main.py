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
    province = {}
    ok = False
    cmd = input('inserisci nome file: ')

    infile = open('province.txt','r')
    for line in infile:
        line = line.strip()
        province[line] = 0.0
    infile.close()

    while not ok:
        try:
            infile = open(cmd,'r')
            ok = True
        except:
            print('RIPROVA')
            cmd = input('inserisci nome file: ')

    for line in infile:
        line = line.strip().split(';')
        if line[2] in province and province[line[2]] < float(line[-1]): province[line[2]] = float(line[-1])
    print()

    for sigla in province:
        print(f"Comune più alto nella provincia di {sigla} e' Roccaverano che si trova a {province[sigla]} metri")

main()