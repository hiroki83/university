#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 08:51:41 2025

@author: hirokiinoue

2. countw(t, w) ritorna il numero di occorrenze della parola w nella stringa t . 
	Esempio
	t = 'le cose non sono solo cose, ma anche cosette'
	countw(t, 'cose') 		ritorna		2

3. digits(t) ritorna la lista delle sequenze numeriche contenute nella stringa t . 
   Per sequenza numerica intendiamo una sequenza di cifre (caratteri 0 , 1 ,…, 9 ) di lunghezza massimale. 
	Esempio
	t = 'via Po n.23, tel. 06 7867555 - cell. 345 675665676 (cc 34565)'
	digits(t) 			ritorna 	['23', '06', '7867555', '345', '675665676', '34565']

4. column(table, k) ritorna una lista che contiene i valori della colonna k della tabella table . 
   La tabella è rappresentata in modo che ogni linea di table contiene una riga e i valori delle colonne sono separati
   dal carattere ';' . Se table ha n colonne, allora ogni linea di table conterrà esattamente n-1 caratteri ';' .
	Esempio
	table = '''Milano;12;23
Roma;16;25
Napoli;15;27
Firenze;11;20'''
	column(table, 1)		ritorna		['12', '16', '15', '11']

##########################################

##########################################

## NOTE

1. Lo standard Unicode è un sistema di codifica di caratteri che assegna un codice numerico univoco ad
ogni carattere di un insieme molto grande che comprende centinaia di migliaia di caratteri relativi a
molte lingue ed alfabeti (latino, greco, cirillico, arabo, cinese, ecc.) e a una moltitudine di simboli
(matematici, geometrici, grafici, ecc.). Però lo standard Unicode non è una codifica di sequenze di byte.
Ci sono molte codifiche che sono compatibili con esso come UTF-8, UTF-16, UTF-32. Ognuno di queste
può codificare in opportune sequenze di byte i codici Unicode. Ad esempio, il carattere à è
rappresentato in UTF-8 da 2 byte c3 a0 , in UTF16 da 4 byte ff fe e0 00 e in UTF-32 da 8 byte ff
fe 00 00 e0 00 00 00 . Queste sono tutte rappresentazioni del codice nello standard Unicode del
carattere à che è 00e0 . ↩
2. Se si vuole conoscere la sequenza di byte, cioè il contenuto grezzo, di una stringa unicode si può usare
la funzione built-in bytes , ad es. bytes(iniziofine, 'raw_unicode_escape') . ↩


## 
"""

"""
## ESERCIZI
Scrivere le funzioni seguenti.

1. firstline(t, s) ritorna la prima linea della stringa t che contiene la stringa s , mentre se s non occorre in t ritorna None . 
	Esempio
>>> t = '''Quant’è bella giovinezza
che si fugge tuttavia!
Chi vuol esser lieto, sia:
del doman non c’è certezza.'''
	firstline(t, 'non')		ritorna		'del doman non c’è certezza.'
"""
def firstline(t s):
    text = splitline(t)