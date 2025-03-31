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
    studenti = []
    outfile = open('sessione.csv','a')
    for appello in ['primo','secondo']:
        infile = open(f'{appello}_appello.csv','r')
        indice = infile.readline()
        for line in infile:
            line = line.strip().split(',')
            studenti.append(line)
        infile.close()


    if len(studenti) >= 5:
        studenti.sort(key=itemgetter(2,1))
        outfile.write(indice)
        for studente in studenti:
            str = ''
            for char in studente: str += f'{char},'
            outfile.write(f'{str[:-1]}\n')
    else : print('NON CI SONO ABBASTANZA STUDENTI')
    outfile.close()

    studenti.sort(key=itemgetter(2),reverse=True)
    media = 0
    for i in range(5):
        media += (float(studenti[i][2]) - float(studenti[i][-1]))
    print(round(media/5,2))

main()