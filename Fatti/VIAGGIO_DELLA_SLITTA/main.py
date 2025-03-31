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

def distanzaCalutator(A,B):
    R = 6731
    lat_A = lat_lon[A][0]
    lon_A = lat_lon[A][1]
    lat_B = lat_lon[B][0]
    lon_B = lat_lon[B][1]
    h = sin((abs(lat_A-lat_B))/2)**2 + cos(lat_A)*cos(lat_B)*sin((abs(lon_A-lon_B))/2)**2
    distanza = 2 * R * asin(sqrt(h))
    return distanza

from math import *
from operator import itemgetter

lat_lon = {}
viaggi = []

infile = open('bambini.csv','r')
indice = infile.readline()
for line in infile:
    line = line.strip().split(',')
    viaggi.append(line)
    if line[-1] not in lat_lon: lat_lon[line[-1]] = [0,0]
infile.close()

infile = open('province.csv','r')
for line in infile:
    line = line.strip().split(',')
    if line[4] in lat_lon: lat_lon[line[4]] = [float(line[-2])*(pi/180),float(line[-1])*(pi/180)]

for i in range(len(viaggi)):
    viaggi[i].extend(lat_lon[viaggi[i][-1]])

viaggi.sort(key=itemgetter(4),reverse=True)
partenza = viaggi[0][3]
print(f'Consegnato {viaggi[0][2]} a {viaggi[0][1]} {viaggi[0][0]} ({viaggi[0][3]})')
print(f'{distanzaCalutator('VE','TO')}Km')
viaggi.pop(0)
min = viaggi[0][3]
indice_min = 0
while len(viaggi)>0:
    min = viaggi[0][3]
    for i in range(len(viaggi)):
        if distanzaCalutator(partenza,viaggi[i][3]) < distanzaCalutator(partenza,min):
            min = viaggi[i][3]
            indice_min = i
    if len(viaggi) == 1: indice_min = 0
    print(f'    {distanzaCalutator(partenza,min)} Km')
    print(f'Consegnato {viaggi[indice_min][2]} a {viaggi[indice_min][1]} {viaggi[indice_min][0]} ({viaggi[indice_min][3]})')
    partenza = min
    viaggi.pop(indice_min)

    
        

