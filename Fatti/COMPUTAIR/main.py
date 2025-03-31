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
    media = []
    weather = {}
    citta = {}
    bad_weather = []

    try:
        infile = open('weather.txt','r')
    except:
        print('ERRORE APERTURA FILE')

    for line in infile:
        line = line.strip().split(';')
        weather[line[0]] = line[1]
    infile.close()

    infile = open('flights.txt','r')
    for line in infile:
        line = line.strip().split(';')
    
        media.append(int(line[2]))

        if line[1] not in citta: citta[line[1]] = int(line[2])
        else: citta[line[1]] += int(line[2])

        if weather[line[1]] in ['Stormy','Rainy']: bad_weather.append(line)
    infile.close()

    print(f'Numero medio di passeggeri: {sum(media)/len(media):0.1f}')
    print()
    print('Codice dei voli verso città con condizione meteorologica Rainy o Stormy:')
    for volo in bad_weather:
        print(f'* {volo[0]} verso {volo[1]}: {weather[volo[1]]}')
    print()
    print('Condizione meteorologica delle città che sono destinazione di almeno un volo:')
    for paesi in citta:
        print(f'* {paesi}: {weather[paesi]}. {citta[paesi]} passeggeri in arrivo.')

main()


