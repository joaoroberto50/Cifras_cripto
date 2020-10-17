# Discentes: João Roberto & Claudionor Amâncio

from lib.caracteres import *
from random import *

#gera uma tabela pra fazer a transposiçao
#quantidade de colunas da tabela = tamanho da chave
def gera_tabela(msg, chave):
    vet = []
    aux = []
    for i in chave:
        aux.append(i)
    vet.append(aux)
    aux = []
    for i in msg:
        aux.append(i)
        if len(aux) == len(chave):
            vet.append(aux)
            aux = []
    if len(aux) != 0:
        vet.append(aux)
    dif = len(vet[len(vet)-2]) - len(vet[len(vet) - 1])
    if dif != 0:
        for i in range(0, dif):
            vet[len(vet)-1].append('y')
    return vet

#encripita fazendo a permuta de colunas da tabela
def encript(msg, chave):
    tabela = gera_tabela(msg, chave)
    aux = []
    tab_cifra = []
    aux_2 = []
    for i in chave:
        aux.append(i)
    aux.sort()
    for i in aux:
        x = tabela[0].index(i)
        for i in range(1, len(tabela)):
            aux_2.append(tabela[i][x])
            if len(aux_2) == len(tabela)-1:
                tab_cifra.append(aux_2)
                aux_2 = []
    return tab_cifra

#reorganiza as colunas da tabela de acordo com a chave da tabela e a chave em ordem
def reorganiza_tab(tabela, chave, key):
    tab_decif = []
    for i in range(0, len(tabela)):
        aux = []
        for j in chave:
            x = key.index(j)
            aux.append(tabela[i][x])
        tab_decif.append(aux)
    tab_decif.pop(0)
    return tab_decif

#decripta reorganizando as colunas e usando a função reorganiza_tabela()
def decript(cifra, chave):
    aux = []
    tab_decif = []
    aux_2 = []
    for i in chave:
        aux.append(i)
    aux.sort()
    tabela = gera_tabela(cifra, aux)
    for i in aux:
        x = tabela[0].index(i)
        for i in range(1, len(tabela)):
            aux_2.append(tabela[i][x])
            if len(aux_2) == len(aux):
                tab_decif.append(aux_2)
                aux_2 = []
    tab_decif = reorganiza_tab(tabela, chave, aux)
    return tab_decif

#gera uma chave aleatoria e sem repetir os caracteres
def gera_Chave(n=7):
    key = ''
    alf_key = lower_case(0)
    for i in range(0, n):
        x = choice(alf_key)
        key += x
        y = alf_key.index(x)
        alf_key.pop(y)
        x = ''
    return key

#recebe a mensagem a ser cifrada e a chave e faz o que tem que fazer
msg = input("Escreva a mensagem que deseja cifrar\n>>> ")
chave  = gera_Chave()
print(chave)
msg = encript(msg, chave)
cifra = ''
for i in range(0, len(msg[0])):
   for j in range(0, len(msg)):
       cifra += msg[j][i]
print(cifra)
cifra = decript(cifra, chave)
msg = ''
for i in range(0, len(cifra)):
   for j in range(0, len(cifra[0])):
       msg += cifra[i][j]
print(msg)


