#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 08:47:52 2025

@author: hirokiinoue

Scrivere le funzioni seguenti.
1. prec(g1, m1, a1, g2, m2, a2) ritorna True se la data g1, m1, a1 (giorno, mese, anno) è precedente
   o uguale alla data g2, m2, a2 .
   Esempi
   prec(13, 11, 2012,  2,  3, 2013)	ritorna	True
   prec(13, 11, 2012, 27, 12, 2011)	ritorna	False
   prec( 1, 10, 2013,  1, 11, 2013)	ritorna	True

2. l2d(lst) che, presa in input una lista lst i cui elementi sono numeri da 0 a 9 espressi in lettere
   ( 'zero' , 'uno' , …, 'nove' ), ritorna una nuova lista i cui elementi sono la traduzione in numeri degli
   elementi di lst . Esempio
   l2d(['nove','due','due','tre'])	ritorna	[9,2,2,3]

3. distinct(lst) ritorna una nuova lista che contiene gli stessi elementi di lst ma senza le eventuali
   ripetizioni.
   Esempi
   distinct([3,1,3,2,6,6])		ritorna	[3, 1, 2, 6]
   distinct(['a','ab','a','ab'])	ritorna	['a', 'ab']

4. search(lst, andc, orc, notc) ritorna una nuova lista di stringhe che contiene le stringhe s della lista
   lst tali che tutte le stringhe della lista andc sono sottostringhe di s, almeno una delle stringhe della
   lista orc (se orc non è vuota) è una sottostringa di s e nessuna delle stringhe della lista notc è una
   sottostringa di s. 
   Esempi, sia lst = ['mela','pera','melo']
   search(lst,['el','a'],['ra','pe','m'],['tt','lo'])	ritorna ['mela']
   search(lst,[],['ra','pe','m'],['tt','lo'])		ritorna ['mela','pera']
   search(lst,['el','a'],[],['tt''lo'])			ritorna ['mela']
   search(lst,[],['ra','pe','m'],[])			ritorna ['mela','pera','melo']
"""

def perc(g1, m1, a1, g2, m2, a2):
    if a1 < a2 or (a1 == a2 and m1 < m2) or (a1 == a2 and m1 == m2 and g1 <= g2):
        return True
    else:
        return False
    
def l2d(lst):
    rtn = []
    for i in range(len(lst)):
        if lst[i]==("zero"):
            rtn += [0]
        elif lst[i]==("uno"):
            rtn += [1]
        elif lst[i]==("due"):
            rtn += [2]
        elif lst[i]==("tre"):
            rtn += [3]
        elif lst[i]==("qattro"):
            rtn += [4]
        elif lst[i]==("cinque"):
            rtn += [5]
        elif lst[i]==("sei"):
            rtn += [6]
        elif lst[i]==("sette"):
            rtn += [7]
        elif lst[i]==("otto"):
            rtn += [8]
        elif lst[i]==("nove"):
            rtn += [9]
    return rtn

def distinct(lst):
    rtn = []
    for i in range(len(lst)):
        if i==0:
            rtn = [lst[i]]
        else:
            for j in range(len(rtn)):
                if lst[i] == rtn[j]:
                    break
            rtn += [lst[i]]
    return rtn