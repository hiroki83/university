#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 18:52:15 2025

@author: hirokiinoue
"""

def fibonacci(num):
    tmp1 = 0
    tmp2 = 1
    sum = 0;
    for anno in range(0,num):
        tmp3 = tmp1 + tmp2;
        '''0=0, 0+1=1, 1+1=2, 1+2=3, 2+3=5'''
        '''print(rtn)'''
        tmp1 = tmp2
        tmp2 = tmp3
        sum += tmp3
    return sum