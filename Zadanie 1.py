# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from numba import njit

@njit
def Zadanie1_21720():
    systems = np.array(['Linux', 'Windows', 'Apple iOS', 'Android', 
                        'Chrome OS'])
    print(type(systems))
    systems[1] = 'Windows 10'
    lista_liczb = np.array([5, 10, 15, 101])
    print(lista_liczb)
    lista_mieszana = np.array(['Python', 3.9, 'Windows', 10, True, False])
    print(lista_mieszana)
    listy_w_liscie = np.array([[2019, [2020, 'XT'], 30], ['Linux', 'Windows', 'QNX'], 
                      2021])
    print(listy_w_liscie)
    hardware = np.array(['x86', 'ARP', 'PowerPC', 'SPARC'])
    software = np.array(['Windows', 'Linux', 'FreeBSD', 'Solaris'])
    platforms = [hardware, software]
    print(platforms)
    print(len(platforms))
    pl = hardware + software
    print(pl)
    print(len(pl))
    pl += ['QNX']
    print(pl)
    lista = np.array([11, 22, 33, 44, 55, 66])
    indx_w_przod = np.array([0, 1, 2, 3, 4, 5,])
    indx_od_tylu = np.array([-6, -5, -4, -3, -2, -1])
    techno = []
    print(techno)    
    techno.append('Python')
    techno.append('java')
    techno.append('java')
    print(techno)
    techno.append(['QNX', 'BSD'])
    print(techno)
    techno = np.array(['Python', 'java'])
    techno.extend(['SQL', 'C++'])
    print(techno)
    techno.insert(0, 'C#')
    print(techno)
    techno.insert(2, 'R')
    print(techno)
Zadanie1_21720()