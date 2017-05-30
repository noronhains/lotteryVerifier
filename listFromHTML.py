# -*- coding: utf-8 -*-
"""
Created on Wed May  3 01:22:40 2017

@author: NoronhaINS
"""

import requests
from bs4 import BeautifulSoup as bs

rLF = requests.get('http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotofacil/')
soupLF = bs(rLF.content, 'html.parser')

rMS = requests.get('http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/')
soupMS = bs(rMS.content, 'html.parser')

def listaSemanaLF():
    listaLF = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    for i in range(15):
        listaLF[i] = soupLF.find_all('td')[i].get_text()
    return listaLF

def listaSemanaMS():
    listaMS = ['', '', '', '', '', '']
    for i in range(70,76):
        listaMS[i-70] = soupMS.find_all('li')[i].get_text()
    return listaMS
