#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 17:51:49 2025

@author: hirokiinoue
"""

'''
## ESERCIZIO

Usando lo schema descritto definite l'algoritmo e il suo pseudo-codice e poi implementate e testate le funzioni e sottofunzioni realizzate.

1)  Modificate la funzione aggiorna_k_massimi in modo da usare una lista ordinata invece che disordinata 
    e misurate i tempi di esecuzione di k_massimi_casuali in Jupyter col comando %time per K=3000 e K=30 (e S=0, N=1000000).

'''
import random
def k_massimi_casuali(N, S, K):
    '''estraggo i K maggiori valori da N generati a caso a partire dal seed S'''
    # inizializzo il seed del generatore con S
    random.seed(N)
    # inizialmente i K valori massimi sono la lista vuota
    result = []
    # genero un valore casuale X alla volta per N volte e ogni volta:
    for i in range(N):
        X = random.randint(-1000000000, 1000000000)
        #ggiorno i K maggiori valori inserendoci X se necessario
        aggiorna_k_massimi(result, X, K)
    # torno i K valori massimi
    #return result

def aggiorna_k_massimi(massimi, V, K):
    '''aggiorno i K massimi aggiungendo un nuovo valore V'''
    # se massimi contiene meno di K valori aggiungiamo
    if len(massimi) < K:
        massimi.append(V)
    # altrimenti se V è minore o uguale del minimo valore contenuto in massimi lo ignoriamo
    elif min(massimi) < V:
        massimi.remove(min(massimi))
        massimi.append(V)
    # altrimenti eliminiamo il minimo ed aggiungiamo V alla lista

def k_massimi_casuali_comprehension(N, S, K):
    '''estraggo i K maggiori valori da N generati a caso a partire dal seed S'''
    # inizializzo il seed del generatore con S
    random.seed(N)
    # inizialmente i K valori massimi sono la lista vuota
    result = []
    # genero un valore casuale X alla volta per N volte e ogni volta:
    for i in range(N):
        X = random.randint(-1000000000, 1000000000)
        #ggiorno i K maggiori valori inserendoci X se necessario
        aggiorna_k_massimi_comprehension(result, X, K)
    # torno i K valori massimi
    return result

def aggiorna_k_massimi_comprehension(massimi, V, K):
    '''aggiorno i K massimi aggiungendo un nuovo valore V in modo ottimizzato'''
    # se massimi contiene meno di K valori aggiungiamo V alla lista mantenendo l'ordine
    if len(massimi) < K:
        add_sorted(massimi, V)
    # altrimenti se V è minore o uguale del minimo valore contenuto in massimi lo ignoriamo
    elif massimi[0] < V:
        massimi.remove(massimi[0])
        add_sorted(massimi, V)
    # altrimenti eliminiamo il minimo ed aggiungiamo V alla lista mantenendo l'ordine

def add_sorted(massimi, V):
    '''aggiungo il valore V nella lista massimi in ordine crescente.'''
    print(V)
    # se massimo è vuota lo aggiungo
    if len(massimi)==0:
        massimi.append(V)
    # se esiste già stesso valore nella lista lo aggiungo insert(index)
    elif V in massimi:
        idx = massimi(V)
        massimi.insert(idx, V)
    # altrimenti se il valore è maggiore o uguale del massimo valore lo aggiungo append()
    elif max(massimi) < V:
        massimi.append(V)
    # altrimenti cerco un valore maggiore, lo appena trovato inserisco prima di lui
    else:
        for i in range(len(massimi)):
            if (massimi[i]>V):
                massimi.insert(i,V)
                break