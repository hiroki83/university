#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 11:47:39 2025

@author: hirokiinoue
"""

# estrrae i K massimi dalla lista L
    # controllo che 0 <= K <= len(L)
    # dichiaro un variabile risultato =[] 
    # ciclo K volte
        # estraggo il valore massimo dalla L
        # lo aggiungo alla lista risultato
    # torna il risultato
def k_max(L, K):
    '''estrrae i K massimi dalla lista L'''
    # controllo che 0 <= K <= len(L)
    assert 0 <= K <= len(L),"il valore di K non è corretto.  0 <= {} <= {} ".format(K,len(L)) 
    # dichiaro un variabile risultato =[] 
    result = []
    # ciclo K volte
    for i in range(K):
        # estraggo il valore massimo dalla L
        maxValue = extract_maxV(L, K)
        # lo aggiungo alla lista risultato
        result.append(maxValue)
    # torna il risultato
    return result

def extract_maxV(L, K):
    '''estraggo il valore massimo dalla lista L'''
    value = 0
    #mettere in ordine la lista
    lista = L
    lista.sort(reverse=True)
    value = lista[0]
    #elimino il valore massimo
    L.remove(value)
    return value