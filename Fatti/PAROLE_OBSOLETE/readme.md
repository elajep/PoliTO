# Testo d'esame "Parole obsolete"

Si realizzi un programma Python che legga un testo letterario `testo.txt` e che lo elabori e ne stampi alcune
statistiche. In particolare il programma deve:

- contare il numero di parole

- leggendo un opportuno file `obsoleto.txt` deve indicare quante volte sono presenti nel testo le parole riportate in tale
  file (numero di occorrenze per ciascuna parola obsoleta); il file `obsoleto.txt` contiene, per ogni riga, una parola di
  uso ormai raro ed in parallelo la parola utilizzata in tempi più recenti

- sempre tramite il file `obsoleto.txt` deve sostituire le parole arcaiche con i vocaboli nuovi riportati nel file stesso,
  stampando quindi il testo letterario nella nuova forma; la nuova forma deve essere stampata nel file `nuovotesto.txt`

Si noti che i file `testo.txt` ed `obsoleto.txt` sono da considerare privi di errori e sono codificati tramite la codifica
`'utf-8'`. La stessa codifica va usata per il file in uscita `nuovotesto.txt`.

## Esempio di file `obsoleto.txt`:

	ivi qui
	curato cappellano
	gocciolo goccio
	bravo ceffo
	ufizio ufficio
	rincomincia ricomincia

## Esempio di file `testo.txt`:

Quel ramo del lago di Como, che volge a mezzogiorno, tra due catene non interrotte di monti, tutto a seni e a golfi, a
seconda dello sporgere e del rientrare di quelli, vien, quasi a un tratto, a ristringersi, e a prender corso e figura di
fiume, tra un promontorio a destra, e un'ampia costiera dall'altra parte; e il ponte, che ivi congiunge le due rive, par
che renda ancor più sensibile all'occhio questa trasformazione, e segni il punto in cui il lago cessa, e l'Adda
rincomincia , per ripigliar poi nome di lago dove le rive, allontanandosi di nuovo, lascian l'acqua distendersi e
rallentarsi in nuovi golfi e in nuovi seni.

## Esempio di file *OUTPUT* `nuovotesto.txt`:

Quel ramo del lago di Como, che volge a mezzogiorno, tra due catene non interrotte di monti, tutto a seni e a golfi, a
seconda dello sporgere e del rientrare di quelli, vien, quasi a un tratto, a ristringersi, e a prender corso e figura di
fiume, tra un promontorio a destra, e un'ampia costiera dall'altra parte; e il ponte, che qui congiunge le due rive, par
che renda ancor più sensibile all'occhio questa trasformazione, e segni il punto in cui il lago cessa, e l'Adda
ricomincia , per ripigliar poi nome di lago dove le rive, allontanandosi di nuovo, lascian l'acqua distendersi e
rallentarsi in nuovi golfi e in nuovi seni.

## Esempio di messaggi stampati a video dal programma:

	Il numero di parole presenti nel testo è: 6182
	Le parole obsolete sono così riportate nel testo originale:
	bravo: 6
	curato: 8
	gocciolo: 1
	ivi: 3
	rincomincia: 1
	ufizio: 1