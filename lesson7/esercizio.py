'''
## ESERCIZI

Usando la list comprehension definite le seguenti funzioni:




################################################################################
'''
'''
1. Definite la funzione triangolo(N) che torna una matrice triangolare di N*N/2 elementi, 
   contenente solo la parte in basso a sinistra della matrice dei prodotti (tabelline).
   Il risultato quindi dev'essere una lista di N liste di lunghezza crescente da 1 a N.
   Esempio:
>>> triangolo(4)
[[1],
 [2, 4],
 [3, 6, 9],
 [4, 8, 12, 16]] 
'''
def triangolo(n):
    rtn = []
    for i in range(1,n+1):
        tmp = []
        for j in range(1,i+1):
            tmp += [i*j]
        rtn += [tmp]
    return rtn

def triangoloWithComprehension(n):
    return [[i*j for i in range(1,j+1)] for j in range(1,n+1)]

'''
2. Definite la funzione potenze_crescenti(lista) che produce come risultato una lista
   in cui ciascun elemento è ottenuto come la potenza i-esima del corrispondente elemento
   in posizione i della lista passata come argomento.
   Esempio:
>>> potenze_crescenti([2, 3, 4, 5, 6])
[1, 3, 16, 125, 1296]

'''
def potenze_crescenti(lista):
    return [
            lista[i]**i
            for i in range(0,len(lista))
        ]

def potenze_crescentiWithEnumerate(lista):
    return [x**i for i, x in enumerate(lista)]

'''
3. Definite la funzione non_divisibili(N, divisori) che trova tutti i numeri tra 1 e N (compresi)
   che non sono divisibili per nessuno dei valori presenti nella lista di divisori (interi).
   Esempio:
>>> non_divisibili(10, [2, 3])
[1, 5, 7]

'''
def non_divisibili(N, divisori):
    rtn = []
    for i in range(1,N+1):
        for j in range(len(divisori)):
            if i%divisori[j]==0:
                break
            elif not j == len(divisori)-1:
                continue
            else:
                rtn+=[i]
    return rtn

def non_divisibiliWithComprehension(N, divisori):
    return [
     i 
     for i in range(1,N+1)
     if len([divisori[j] for j in range(len(divisori)) if i%divisori[j]==0])==0
     ]

def helper_non_divisibiliWithComprehension(v, divisori):
    return [True for i in range(len(divisori)) if v%divisori[i]==0]

def non_divisibiliWithSet(N, divisori):
    divisibili = {x for x in range(1,N+1) for y in divisori if x%y==0}
    '''print(divisibili)'''
    return [y for y in range(1,N+1) if y not in divisibili]
    
'''
4.  Definite la funzione doppio_dado() che stampa una successione di estrazioni casuali di due dadi a 6 facce 
    e che conta e torna come risultato quante ne sono state necessarie prima di ottenere un doppio 6.
    Esempio:
>>> doppio_dado()
3 5
2 2
1 6
6 4
3 1
5 4
6 6
7
'''
import random
def doppio_dado():
    '''print(random.randint(1,6))'''
    dado1,dado2 = random.randint(1,6), random.randint(1,6)
    '''dado1,dado2=6,6'''
    cnt = 0
    while (dado1,dado2) != (6,6):
        print(dado1, dado2)
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        cnt+=1
    else:
        print(dado1, dado2)
        cnt+=1
        print(cnt)
    return cnt

def doppio_dadoComprehension():
    conteggio = 0
    d1,d2 = 0,0
    while (d1,d2) != (6,6):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        print(d1,d2)
        conteggio+=1
    return conteggio