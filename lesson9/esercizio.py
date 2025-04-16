#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 08:01:23 2025

@author: hirokiinoue
"""

'''
## ESERCIZI

Scrivere le funzioni seguenti.

1. clines(fname, s) ritorna il numero di linee del file di testo fname che contengono la stringa s senza
   differenziare tra maiuscole e minuscole. Esempi: se il file testo.txt contiene le 4 righe

SUGLI ERRORI
Gli errori sono inevitabili. Errare è umano,
perseverare è diabolico. Non ci sono rimedi
a questo stato di cose (su questa terra).

allora
	clines('testo.txt', 'err')	ritorna 3
	clines('testo.txt', 'Errori')	ritorna 2
'''
def clines(fname, s):
    cnt = 0
    with open(fname) as f:
        for i, linea in enumerate(f):
            if s.upper() in linea.upper():
                cnt += 1
    return cnt

'''

2. all_char(fname, enc) ritorna una stringa unicode contenente tutti i caratteri, senza ripetizioni e in
   ordine di apparizione, nel file fname decodificato con la codifica enc . Ad esempio se il file è quello
   dell'esercizio precedente, assumendo che sia codificato in UTF-8, si ha:

       SUGLI ERRORI
       Gli errori sono inevitabili. Errare è umano,
       perseverare è diabolico. Non ci sono rimedi
       a questo stato di cose (su questa terra).

>>> allc = all_char('testo.txt', 'utf8')
>>> allc
'SUGLI ERO\nlierosnvtab.èum,pdcNq()'
>>> print(allc)
SUGLI ERO
lierosnvtab.èum,pdcNq()
'''
def all_char(fname, enc):
    result = ''
    with open(fname, encoding=enc) as f:
        text = f.read()
        for i in range(len(text)):
            if not text[i] in result:
                result += (text[i])
    return result
'''

3. anagrams(fname, w) ritorna una lista contenente tutti gli anagrammi, senza ripetizioni e senza
   differenziare tra maiuscole e minuscole, della parola w nel file fname . Un anagramma di una parola w è
   un'altra parola che usa esattamente le stesse lettere di w ma in ordine diverso, ad esempio mangiare e
   germania, torre e retro. La lista ritornata deve includere anche la parola w stessa, se è presente.
   Possono risultare utili la funzione built-in sorted() e il metodo join() delle stringhe.
   Nel risultato non ci devono essere doppioni.
   Esempi, sia fname il file 'alice.txt' :

>>> anagrams(fname, 'read')	ritorna ['dear', 'read', 'dare']
>>> anagrams(fname, 'elbow')	ritorna ['elbow', 'below']

'''

'''
4. log_update(filelog, evento) aggiorna il file filelog aggiungendo una nuova linea che inizia con la data e l'orario
   della chiamata e dopo ': ' la stringa in evento . Per ottenere la data e l'orario si possono usare le funzioni
   ctime() e time() del modulo time della libreria standard. Esempio, se il file log contiene:

Mon Oct 7 17:48:22 2013: first event
Mon Oct 7 17:48:32 2013: second event
Mon Oct 7 17:49:15 2013: Event n. 3

e se dopo 84 secondi dall'ultimo aggiornamento viene effettuata la chiamata log_update(log, 'New event!') , il file log diventa:

Mon Oct 7 17:48:22 2013: first event
Mon Oct 7 17:48:32 2013: second event
Mon Oct 7 17:49:15 2013: Event n. 3
Mon Oct 7 17:50:39 2013: New event!


5. findurl(lista_url, s, k) ritorna in una lista gli URL contenuti nella lista lista_urls tali che le pagine da essi puntate contengano almeno k
   occorrenze della stringa s . Si assume che gli URL in urls siano relativi a pagine HTML e quindi documenti di testo. 
   Esempi, sia

>>> urls = ['http://python.org', 'http://google.com', 'http://docs.python.org/2.7/index.html', 'http://pellacini.di.uniroma1.it/teaching/fondamenti13/index.html']
>>> findurl(urls, 'Python', 2) ritorna 
['http://python.org', 'http://docs.python.org/2.7/index.html', 'http://pellacini.di.uniroma1.it/teaching/fondamenti13/index.html'] 
>>> findurl(urls, 'Python', 7) ritorna 
['http://python.org', 'http://docs.python.org/2.7/index.html']
'''

