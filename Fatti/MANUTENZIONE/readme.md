# Testo d'esame "Manutenzione Macchine"

Il file `manutenzione.txt` contiene la lista delle manutenzioni effettuate o da effettuare sulla propria autovettura e
la data in cui vanno effettuate o sono state effettuate. Ogni riga del file corrisponde ad una operazione, ed è composta
dal nome dell'operazione e dalla data (gg/mm/aaaa) in cui l'operazione è stata effettuata o da effettuare e il costo
della manutenzione. I campi sono separati da virgola e le operazioni non sono elencate secondo un particolare ordine.
Tutte le date sono successive al 1/1/2017.

In un secondo file di nome `parametri.txt` il programma riceve le seguenti informazioni, contenute nella prima ed **unica**
riga del file e separate da virgola: una data nel formato gg/mm/aaaa e un parametro `a` o `p`.

## Esempio del file `parametri.txt`:

    26/08/2018,a

Il programma dovrà stampare a schermo in ordine di data le operazioni effettuate prima della data inserita se è stato
specificato il parametro `a` o quelle da effettuare in futuro se il parametro è `p`. In entrambi i casi si deve
stampare la manutenzione più cara nel periodo in analisi.

## Esempio di file `manutenzione.txt`:

    Pulitura,15/08/2018,50
    Lavaggio,12/09/2019,20 
    Lucidatura,25/08/2018,50
    Controllo Testata,23/07/2017,200
    Controllo Cilindro,17/09/2019,150

## Messaggi stampati a video dal programma:

**Esempio 1:**

Se `parametri.txt` contiene:

    data: 26/08/2018
    parametro: a

L'output sarà:

    Le operazioni effettuate prima del 26/08/2018 sono:

      Controllo Testata in data 23/7/2017 costo 200 euro
      Pulitura in data 15/8/2018 costo 50 euro
      Lucidatura in data 25/8/2018 costo 50 euro

    La manutenzione più costosa è stata Controllo Testata del 23/7/2017 costata 200 euro

**Esempio 2:** (con parametro `p`)

Se `parametri.txt` contiene:

    data: 26/08/2018
    parametro: p

L'output sarà:

    Le operazioni da effettuare dopo il 26/08/2018 sono:
      Lavaggio in data 12/9/2019 costo 20 euro
      Controllo Cilindro in data 17/9/2019 costo 150 euro

    La manutenzione più costosa da effetuare è Controllo Cilindro in data 23/7/2017 costata 150 euro