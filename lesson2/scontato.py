# -*- coding: utf-8 -*-
"""
1. Scrivere una funzione ’scontato’ che prende in input un importo e una percentu-
ale di sconto e ritorna l’importo scontato. Ad esempio, se l’importo è 1000 e 
lo sconto è 20, la funzione ritorna 800.
"""
import math

def scontato(importo, percetuale):
    return round(importo * (1-percetuale/100))

"""
Scrivere una funzione ’secondi’ che prende in input un lasso di tempo espresso 
tramite numero di ore hh, numero di minuti mm e numero secondi ss e ritorna 
l’equivalente numero di secondi. Ad esempio, se hh=2, mm=1 e ss=11, la funzione
 ritorna 7271.
"""
def secondi(hh, mm, ss):
    return hh*3600+mm*60+ss;

"""
3. Scrivere una funzione ‘invest’ che prende in input un capitale C, un intere-
sse annuale i e un numero di anni n e ritorna come intero il capitale maturato 
dopo un investimento di n anni all’interesse i. 
(Usando la formula maturato = capitale * (1+intresse/100)**anni)
Ad esempio, se gli argomenti sono C=1000, i=10 e n=2, la funzione ritorna 1210.
"""

def invest(capitale, interesse, anni):
    print(capitale*(1+interesse/100))
    print(capitale*(1+interesse/100)*(1+interesse/100)) 
    print(round(capitale*((1+interesse/100)**anni)))
    print(round((capitale*(1+interesse/100))**anni))
    print(1100**2)
    print(1000*(1.1**2))
    print(1.1**2)
    print(1100*1.1)
    print(1000*1.1+1100*1.1)
    print(1100*0.1)
    print(1000*0.1+1100*0.1)
    return round(capitale*(1+interesse/100)**anni)