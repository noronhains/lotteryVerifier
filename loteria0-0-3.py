# -*- coding: utf-8 -*-
"""
Created on Wed May  3 01:28:45 2017

@author: NoronhaINS
"""
from listFromHTML import listaSemanaLF
from listFromHTML import listaSemanaMS
import numpy as np

saida = 's'

while saida == 's':
    quest1 = input('O que você gostaria de fazer?\n1-Verificar jogos       2-Adicionar jogos(não implementado) ---> ')
    print('\n')
    if quest1 == '1':
    
        quest2 = input('Quais jogos você gostaria de verificar?\n1-Megasena       2-Lotofácil ---> ')
        print('\n')
#--------------------------------------MEGASENA-----------------------------------------------------    
        if quest2 == '1':
        
            c = 0
            lista = listaSemanaMS() #método do arquivo listFromHTML.py onde ele cria uma lista com os valores do resultado semanal via BeautifulSoap e requests
            jogoSemana = np.array(lista) #transformando a lista em um array numpy
            
            arqJogos = np.loadtxt('arqJogosMS.txt', delimiter = ',') #carregando os dados do arquivo arqJogos.txt e transformando em array
            
            for jogoNum in range(len(arqJogos)): #loop na quantidade de linhas do arquivo
            
                for i in arqJogos[jogoNum]: #loop nas linhas do arquivo
                    for j in jogoSemana: #loop no array do reultado semanal
                        if int(i) == int(j): #comparando o resultado com os jogos
                            c += 1 #contador é acrescentado caso tenha números iguais
                if c == 6:
                    print('PARABÉNS, VOCÊ FOI O GANHADOR! Você acertou %d números no jogo %d. Vá pegar o seu prêmio.'%(c, jogoNum + 1))
                elif c == 5:
                    print('Parabéns! Você acertou %d números no jogo %d. Vá pegar o seu prêmio.'%(c, jogoNum + 1))
                elif c == 4:
                    print('Parabéns! Você acertou %d números no jogo %d. Vá pegar o seu prêmio.'%(c, jogoNum + 1))
                else:
                    print('Infelizmente você não ganhou nada. Você acertou %d números no jogo %d.'%(c, jogoNum + 1))
       
                c = 0
    
            print('\n\n')    
 #------------------------------------LOTOFÁCIL----------------------------------------------------       
        elif quest2 == '2':
            
            c = 0
            lista = listaSemanaLF() #método do arquivo listFromHTML.py onde ele cria uma lista com os valores do resultado semanal via BeautifulSoap e requests
            jogoSemana = np.array(lista) #transformando a lista em um array numpy
        
            arqJogos = np.loadtxt('arqJogosLF.txt', delimiter = ',') #carregando os dados do arquivo arqJogos.txt e transformando em array
            
            for jogoNum in range(len(arqJogos)): #loop na quantidade de linhas do arquivo
            
                for i in arqJogos[jogoNum]: #loop nas linhas do arquivo
                    for j in jogoSemana: #loop no array do reultado semanal
                        if int(i) == int(j): #comparando o resultado com os jogos
                            c += 1 #contador é acrescentado caso tenha números iguais
                if c == 15:
                    print('PARABÉNS, VOCÊ FOI O GANHADOR! Você acertou %d números no jogo %d. Vá pegar o seu prêmio.'%(c, jogoNum + 1))
                elif c == 14:
                    print('Parabéns! Você acertou %d números no jogo %d. Vá pegar o seu prêmio.'%(c, jogoNum + 1))
                elif c == 13:
                    print('Parabéns! Você acertou %d números no jogo %d. Vá pegar o seu prêmio.'%(c, jogoNum + 1))
                elif c == 12:
                    print('Parabéns! Você acertou %d números no jogo %d. Vá pegar o seu prêmio.'%(c, jogoNum + 1))
                elif c == 11:
                    print('Parabéns! Você acertou %d números no jogo %d. Vá pegar o seu prêmio.'%(c, jogoNum + 1))
                else:
                    print('Infelizmente você não ganhou nada. Você acertou %d números no jogo %d.'%(c, jogoNum + 1))
       
                c = 0
    
            print('\n\n') 
    
    
    elif quest1 == '2':
        questAdd = input('Qual jogo você gostaria de adicionar?\n1-Megasena       2-Lotofácil ---> ')

# --------------------------------------MEGASENA-----------------------------------------------------
        if questAdd == '1':
            jogoAdd = ['','','','','','']
            for z in range(6):
                jogoAdd[z] = input('Digite o numero de posição %d ---> ' %(z+1))
            arq = open('arqJogosMS.txt', 'a')
            arq.write('\n%s,%s,%s,%s,%s,%s'%(jogoAdd[0],jogoAdd[1],jogoAdd[2],jogoAdd[3],jogoAdd[4],jogoAdd[5]))
            arq.close()
# ------------------------------------LOTOFÁCIL----------------------------------------------------
        elif questAdd == '2':
            jogoAdd = ['', '', '', '', '', '','','','','','','','','','']
            for z in range(15):
                jogoAdd[z] = input('Digite o numero de posição %d ---> ' %(z+1))
            arq = open('arqJogosLF.txt', 'a')
            arq.write('\n%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s'%(jogoAdd[0],jogoAdd[1],jogoAdd[2],jogoAdd[3],jogoAdd[4],jogoAdd[5],jogoAdd[6],jogoAdd[7],jogoAdd[8],jogoAdd[9],jogoAdd[10],jogoAdd[11],jogoAdd[12],jogoAdd[13],jogoAdd[14]))
            arq.close()

    else:
        print('Digite uma opção válida')
            
    saida = input('Deseja continuar? S ou N ---> ').lower()
    

