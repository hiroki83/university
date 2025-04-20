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
        #for i in range(len(text)):
        for i in text:
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
import modules.words as ww
def anagrams(fname, w):
    result = []
    with open(fname) as f:
        text = f.read()
        wordList = ww.words(text)
        for word in wordList:
            if len(w) == len(word) and not word in result:
                flg = True
                for rword in result:
                    if (word.lower() == rword.lower()):
                        flg = False
                        break
                #print(word, ' - ', result)
                if flg:
                    for char in w:
                        if not char.lower() in word.lower():
                            flg = False
                            break
                if flg:
                    result.append(word)
    return result
# La funzione del metodo anagrams(fname, w)
# per trovare gli anagrammi in un file della parola w
    # all'inizio il risultato è una lista vuota
    # convertiamo la parola w in minuscolo
    # leggiamo dal file il suo contenuto e lo convertiamo in minuscole
    # per ogni parola
        # se NON è già apparsa ed è un anagramma della parola w
            # la aggiungiamo al risultato
    # alla fine torniamo la lista di anagrammi
def anagrams_enhanced(fname, wx):
    result = []
    wx = wx.lower()
    with open(fname) as f:
        text = f.read().lower()
        #print(text [100:110])
        wordList = testo_to_parole(text)
        #print(wordList[100:103])
        for wd in wordList:
            #print(wd)
            if not wd in result and sono_anagrammi(wd, wx):
                result.append(wd)
    return result

# La funzione del metodo testo_to_parole(testo):
# per ottenere le parole di un testo
    # all'inizio la lista è vuota
    # all'inizio la parola corrente non contiene nessun carattere
    # scandiamo i caratteri del testo
        # se il carattere corrente è alfabetico
            # lo aggiungiamo alla parola corrente
        # altrimenti
            # la parola corrente è finita e la spostiamo nella lista delle parole
            # e azzeriamo la parola corrente
    # se alla fine la parola corrente non è vuota vuol dire che il testo finiva con una parola 
        # e quindi la aggiungiamo alle parole
    # torniamo le parole trovate

def testo_to_parole(testo):
    parole = []
    parola = ''
    for ch in testo:
        if ch.isalpha():
            parola += ch
        else:
            if len(parola) > 0:
                parole.append(parola)
            parola = ''
    if len(parola) > 0:
        parole.append(parola)
    return parole
# La seconda funzione ausiliaria sono_anagrammi(parola1, parola2)
# per controllare se parola1 e parola2 sono anagrammi
    # costruisco la lista ordinata dei caratteri di parola1
    # costruisco la lista ordinata dei caratteri di parola2
    # torno come risultato il risultato del loro confronto (se sono uguali torna True)
def sono_anagrammi(parola1, parola2):
    #parola1_chars,parola2_chars = [],[]
    #parola1_chars += parola1
    #parola2_chars += parola2
    #parola1_chars.sort()
    #parola2_chars.sort()
    #print(''.join(parola1_chars), ''.join(parola2_chars))
    #if (''.join(parola1_chars) == ''.join(parola2_chars)):
    #    return True
    #else:
    #    return False
    #print(parola1, parola2)
    p1sorted = sorted(parola1)
    p2sorted = sorted(parola2)
    return p1sorted == p2sorted
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
'''
# per aggiungere un evento ad un file di log
    # leggiamo il time corrente
    # lo convertiamo in una stringa che indica la data/ora
    # apriamo il file di log in modalità testo, append
        # scriviamo nel file la riga di testo
import time
import os
def log_update(filelog, evento):
    lines = []
    try:
        with open(filelog, mode='r+') as f:
            lines = f.readlines()
    except:
        print('file not exist!')
    with open(filelog, mode='a') as f:
        if (len(lines) > 0):
            f.write(os.linesep)
        f.write(time.ctime() + ': ' + evento)
    with open(filelog, mode='r') as f:
        print(f.read())
'''

5. findurl(lista_url, s, k) ritorna in una lista gli URL contenuti nella lista lista_urls 
   tali che le pagine da essi puntate contengano almeno k occorrenze della stringa s . 
   Si assume che gli URL in urls siano relativi a pagine HTML e quindi documenti di testo. 
   Esempi, sia

>>> urls = ['http://python.org', 'http://google.com', 'http://docs.python.org/2.7/index.html', 'http://pellacini.di.uniroma1.it/teaching/fondamenti13/index.html']
>>> findurl(urls, 'Python', 2) ritorna 
['http://python.org', 'http://docs.python.org/2.7/index.html', 'http://pellacini.di.uniroma1.it/teaching/fondamenti13/index.html'] 
>>> findurl(urls, 'Python', 7) ritorna 
['http://python.org', 'http://docs.python.org/2.7/index.html']
'''

# per ottenere gli url che contengono almeno k volte la parola s
    # all'inizio il risultato è vuoto
    # per ogni url tra quelli passati
        # leggiamo il contenuto della pagina corrispondente
        # contiamo quante volte ci appare la parola s
        # se il conto è maggiore o uguale k
            # aggiungiamo lo url al risultato
    # alla fine torniamo gli url raccolti
import requests
def findurl(lista_url, s, k):
    result = []
    for url in lista_url:
        with requests.get(url) as f:
            page = f.text
            lista_word = ww.words(page)
            #cnt = 0
            #for wd in lista_word:
            #    if s == wd:
            #        cnt += 1
            cnt = page.count(s)
            if cnt >= k:
                result.append(url)
    return result