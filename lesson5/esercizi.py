#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 00:09:58 2025

@author: hirokiinoue
"""

"""
## ESERCIZI

Scrivere le funzioni seguenti.
1. occ(lst, v) ritorna una lista contenente gli indici delle occorrenze di v nella lista lst . 
   Esempi, sia	lst = ['red','blue','red','gray','yellow','red']
	occ(lst, 'red')		ritorna [0,2,5]
	occ(lst, 'green')	ritorna []
"""
def occ(lst, v):
    rtn = []
    """for i in range(len(lst)):
        if v == lst[i]:
            rtn += [i]
    """
    for i, X in enumerate(lst):
        if X == v:
            rtn.append(i)
    return rtn

"""
2. rep(lst, k) ritorna una lista, senza ripetizioni, che contiene i valori che nella lista lst occorrono
   almeno k volte. 
   Esempi, sia lst = [1,2,1,5,3,4,2,1,3,5,6]

	rep(lst, 2)	ritorna [1,2,5,3]
	rep(lst, 3)	ritorna [1]
	rep(lst, 4)	ritorna []
"""
def rep(lst, k):
    rtn = []
    for i in range(len(lst)):
        cnt = 0
        if lst[i] in rtn:
            continue
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                cnt += 1
        if cnt >= k:
            rtn += [lst[i]]
    return rtn

"""
3. lastfirst(lst) presa in input una lista lst di parole, ritorna la prima parola che inizia con un
   carattere diverso dall'ultimo carattere della parola precedente, se non c'è ritorna None . 
   Esempi
	lastfirst(['sole','elmo','orco','alba','asta'])		ritorna 'alba'
	lastfirst(['sky','you','use','ear','right'])		ritorna None
"""

def lastfirst(lst):
    for i in range(len(lst)-1):
        if lst[i][len(lst[i])-1] != lst[i+1][0]:
            return lst[i+1]
    return None

"""
4. groupd(lst) presa in input una lista lst di interi tale che i primi tre rappresentano una data, 
   i secondi tre un'altra data, i successivi tre un'altra data e così via, 
   modifica la lista lst raggruppando ogni tripla in una stringa separando i numeri con il carattere '/' . 
   Si assume che la lista lst abbia una lunghezza multipla di 3. 
   Esempio
>>> lst = [1, 2, 2013, 23, 9, 2011, 10, 11, 2000]
>>> groupd(lst)
>>> lst
['1/2/2013', '23/9/2011', '10/11/2000']
"""
def groupd(lst):
    for i in range(len(lst)//3):
        dd, mm, yy = lst[i:i+3]
        lst[i:i+3] = [str(dd) + '/' + str(mm) + '/' + str(yy)]
    """
    for i in range(len(lst)):
       if i == 0 or i%3==0:
           rtn += [str(lst[i]) + '/' + str(lst[i+1]) + '/' + str(lst[i+2])]
    lst.clear()
    lst += rtn
    """