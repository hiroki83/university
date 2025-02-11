#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 18:24:24 2025

@author: hirokiinoue
"""

def cubi(list):
    cubiList = []
    for element in list:
        cubiList = cubiList + [element**4]
    return cubiList