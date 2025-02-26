#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 08:47:52 2025

@author: hirokiinoue

"""

"""
Scrivere le funzioni seguenti.
1. prec(g1, m1, a1, g2, m2, a2) ritorna True se la data g1, m1, a1 (giorno, mese, anno) è precedente
   o uguale alla data g2, m2, a2 .
   Esempi
   prec(13, 11, 2012,  2,  3, 2013)	ritorna	True
   prec(13, 11, 2012, 27, 12, 2011)	ritorna	False
   prec( 1, 10, 2013,  1, 11, 2013)	ritorna	True
"""
def perc(g1, m1, a1, g2, m2, a2):
    if a1 < a2 or (a1 == a2 and m1 < m2) or (a1 == a2 and m1 == m2 and g1 <= g2):
        return True
    else:
        return False

"""
2. l2d(lst) che, presa in input una lista lst i cui elementi sono numeri da 0 a 9 espressi in lettere
   ( 'zero' , 'uno' , …, 'nove' ), ritorna una nuova lista i cui elementi sono la traduzione in numeri degli
   elementi di lst . Esempio
   l2d(['nove','due','due','tre'])	ritorna	[9,2,2,3]
"""
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

"""
3. distinct(lst) ritorna una nuova lista che contiene gli stessi elementi di lst ma senza le eventuali
   ripetizioni.
   Esempi
   distinct([3,1,3,2,6,6])		ritorna	[3, 1, 2, 6]
   distinct(['a','ab','a','ab'])	ritorna	['a', 'ab']
"""
def distinct(lst):
    rtn = [lst[0]]
    for i in range(len(lst)):
        flg = False
        for j in range(len(rtn)):
            if lst[i] == rtn[j]:
                flg = True
        if flg == False:
            rtn += [lst[i]]
    return rtn

"""
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
def search(lst, andc, orc, notc):
    rtn = []
    flg1 = False
    andcTmp = []
    orcTmp = []
    notcTmp = []
    """1. check andc"""
    for i in range(len(lst)):
        for j in range(len(andc)):
            if contains(lst[i], len(lst[i]), andc[j], len(andc[j]), 0):
                flg1=True
            else:
                flg1=False
                break
        if flg1:
            andcTmp += [lst[i]]
    rtn = andcTmp
    """if andc is empty set all components of lst in andcTmp"""
    if len(andc) == 0:
        andcTmp = lst
    print("andcTmp: ", andcTmp)
    for i in range(len(andcTmp)):
        for j in range(len(orc)):
            print("andcTmp[i]=",andcTmp[i], " orc[j]=", orc[j])
            if contains(andcTmp[i], len(andcTmp[i]), orc[j], len(orc[j]), 0):
                orcTmp += [andcTmp[i]]
                break
    rtn = orcTmp
    """if orc is empty set all components of andcTmp in orcTmp"""
    if len(orc) == 0:
        orcTmp = andcTmp
    print("orcTmp: ", orcTmp)
    flg1 = False
    for i in range(len(orcTmp)):
        for j in range(len(notc)):
            print("orcTmp[i]=",orcTmp[i], " notc[j]=", notc[j])
            if contains(orcTmp[i], len(orcTmp[i]), notc[j], len(notc[j]), 0):
                flg1=False
                break
            else:
                flg1=True
        if flg1:
            notcTmp += [orcTmp[i]]
    if len(notc) == 0:
        notcTmp = orcTmp
    rtn = notcTmp
    return rtn

def contains(s1, len1, s2, len2, cnt):
    ary1 = []
    ary2 = []
    ary1 += s1
    ary2 += s2
    for i in range(len(ary1)):
        for j in range(len(ary2)):
            """match both chars"""
            if ary1[i] == ary2[j]:
                """print(ary1, ary2,i,j,cnt)"""
                cnt+=1
                if cnt == len2:
                    return True
                else:
                    tmp1 = ""
                    tmp2 = ""
                    idx1 = i+1
                    idx2 = j+1
                    """recursive the method contains()"""
                    for k in range(len(ary1)-idx1):
                        tmp1 += ary1[idx1]
                        idx1+=1
                    for l in range(len(ary2)-idx2): 
                        tmp2 += ary2[idx2]
                        idx2+=1
                    if contains(tmp1, len1, tmp2, len2, cnt):
                        return True
            elif len(s1) == len(s2) and j == 0:
                return False
    return False