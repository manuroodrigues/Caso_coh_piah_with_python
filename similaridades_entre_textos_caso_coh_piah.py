# -*- coding: utf-8 -*-
"""Similaridades entre textos - Caso COH-PIAH.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vB4G9nPsvz4wFdU_2guSitXWRYHwSesC
"""

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto" + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter sair):")

    return textos

def separa_setencas(texto):
    '''A funcao recebe um texto e devolve uma  lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas [-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
      
    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao revebe uma lista de palavras e devolve o numero de paravras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1 
    return len(freq)

def n_palavras(texto):
    return len(lista_palavras(texto))

def caractere_palavras(texto):
    stnc = separa_sentencas(texto)
    frs = list()
    for i in stnc:
        x = separa_frases(i)
        frs += x
    plvr = list()
    for i in frs:
        x = separa_palavras(i)
        plvr += x
        
    s = 0
    for i in plvr:
        s += len(i)
    return s

def caractere_sentencas(texto):
    stnc = separa_sentencas(texto)
    frs = 0
    for i in stnc:
        x = len(i)
        frs += x
    return frs

def caractere_frases(texto):
    stnc = separa_sentencas(texto)
    frs = list()
    for i in stnc:
        x = separa_frases(i)
        frs += x
    plvr = 0
    for i in frs:
        x = len(i)
        plvr += x
    return plvr

def conta_frases(texto):
    c = separa_sentencas(texto)
    frases = []
    for w in c:
        f = separa_frases(w)
        frases += f
    return len(frases)

def conta_sentencas(texto):
    return len(separa_sentencas(texto))

def lista_palavras(texto):
    stnc = separa_sentencas(texto)
    frs = list()
    for i in stnc:
        x = separa_frases(i)
        frs += x
    plvr = list()
    for i in frs:
        x = separa_palavras(i)
        plvr += x
    return plvr

def wal(texto):
    return caractere_palavras(texto) / n_palavras(texto)

def ttr(texto):
    return n_palavras_diferentes(lista_palavras(texto)) / n_palavras(texto)

def hlr(texto):
    return n_palavras_unicas(lista_palavras(texto)) / n_palavras(texto)

def sal(texto):
    return caractere_sentencas(texto) / conta_sentencas(texto)

def sac(texto):
    return conta_frases(texto) / conta_sentencas(texto)

def pal(texto):
    return caractere_frases(texto) / conta_frases(texto)
      

def compara_assinatura(as_a, as_b):
    i = 0
    x = 0
    s = 0
    ca = list()
    while i<=5:
        x = ass_cp[i]-as_b[i]
        if x<0:
            ca.append(x*-1)
        else:
            ca.append(x)
        i += 1
    
    for i in ca:
        x = i
        s += x
    
    return s/6
    pass

def calcula_assinatura(texto):
    vwal = wal(texto)
    vttr = ttr(texto)
    vhlr = hlr(texto)
    vsal = sal(texto)
    vsac = sac(texto)
    vpal = pal(texto)
    return [vwal, vttr, vhlr, vsal, vsac, vpal]

    pass

def avalia_textos(textos, ass_cp):
    ca = []
    for i in lista_textos:
        as_b = calcula_assinatura(i)
        ca.append(as_b)
    cpa = []
    for i in ca:
        x = compara_assinatura(ass_cp,i)
        cpa.append(x)
    return cpa.index(min(cpa))+1

    pass


ass_cp = le_assinatura()

lista_textos = le_textos()

print ('O autor do texto', avalia_textos(lista_textos, ass_cp), 'está infectado com COH-PIAH')