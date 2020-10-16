# Discentes: João Roberto & Claudionor Amâncio

from lib.caracteres import *
from random import choice

#vai definir uma tabela apenas de minusculos e vai retirar o char 'j'
alf = lower_case(0)
alf.pop(9)

#vai separar as silabas, caracteres iguais em sequencia ex: 'ss' por sw e ws
#Aida tabem subistitui ' ' por 'w' e adiciona 'w'
def separa_silaba(msg):
    palavra = []
    silaba = ''
    for i in msg:
        if i == 'j':
            i = 'i'
        if i == ' ':
            i = 'w'
        silaba+=i
        if len(silaba) == 2:
            if silaba[0]==silaba[1]:
                silaba = silaba[1]
                silaba+='w'
                palavra.append(silaba)
                silaba= 'w'+silaba[0]
                palavra.append(silaba)
            else:
                palavra.append(silaba)
            silaba = ''
    if silaba != '':
        silaba+= 'w'
        palavra.append(silaba)
    return palavra

#vai modificar a tabela adicionando a chave
#cria uma tabela com qualquer chave e de qualquer tamanho
def modifica_tabela(alf, key):
    ABC = []
    aux = []
    cont=0
    for i in key:
        cont+=1
        aux.append(i)
        i = alf.index(i)
        alf.pop(i)
        if len(aux) == 5 or cont == len(key):
            ABC.append(aux)
            aux = []
    if len(ABC[len(ABC)-1]) >= 5:
        ABC.append([])
    if len(ABC[len(ABC)-1]) != 0:
        dif = len(ABC[len(ABC)-1])
    else:
        dif = 0
    for i in range((len(ABC)-1), 5):
        for j in range((len(ABC[i])-1), 4):
            x = ((i+1)-(len(ABC)-(i-1))) * 5 + ((j+1))-dif
            if x < len(alf):
                ABC[i].append(alf[x])
        if len(ABC) < 5:
            ABC.append([])
    if len(ABC) > 5:
        ABC.pop()
    return ABC

#Acha a posiçao do caracter na tabela
def found_posi(ctr, ALFB):
    for i in range(0, 5):
        for j in range(0, 5):
            if ALFB[i][j] == ctr:
                return [i, j]

#Faz a criptografia
#achando a posição em ALFB, armazenando nas variaveis a e b (que sao vetores)
#se um desses valores do vetor de a for igual ao de b, siguinifica: mesma linha ou coluna então vai andar para baixo e ou para direita
#se forem diferentes a[1] = b[1] e b[1] = a[1]
def encript(msg, ALFB):
    cifra = ''
    for i in msg:
        a = found_posi(i[0], ALFB)
        b = found_posi(i[1], ALFB)
        if a[0] == b[0]:
            a[1]+=1
            if a[1] > 4:
                a[1] = 0
            b[1]+=1
            if b[1] > 4:
                b[1] = 0
        elif a[1] == b[1]:
            a[0]+=1
            if a[0] > 4:
                a[0] = 0
            b[0]+=1
            if b[0] > 4:
                b[0] = 0
        else:
            c = a[1]
            a[1]=b[1]
            b[1]=c
        cifra+= ALFB[a[0]][a[1]]
        cifra+= ALFB[b[0]][b[1]]
    return cifra

#decripitar, a mesma coisa de encripitar, so que andando pra cima e para esquerda
def decript(cifra, ALFB):
    msg = ''
    for i in cifra:
        a = found_posi(i[0], ALFB)
        b = found_posi(i[1], ALFB)
        if a[0] == b[0]:
            a[1] -= 1
            if a[1] < 0:
                a[1] = 4
            b[1] -= 1
            if b[1] < 0:
                b[1] = 4
        elif a[1] == b[1]:
            a[0] -= 1
            if a[0] < 0:
                a[0] = 4
            b[0] -= 1
            if b[0] < 0:
                b[0] = 4
        else:
            c = a[1]
            a[1] = b[1]
            b[1] = c
        msg += ALFB[a[0]][a[1]]
        msg += ALFB[b[0]][b[1]]
    return msg

#vai gerar uma chave aleatoria de qualquer tamanho
def gera_Key(n_char):
    key = ''
    afb = lower_case(0)
    afb.pop(9)
    for i in range(0, n_char):
        ctr = choice(afb)
        key += ctr
        x = afb.index(ctr)
        afb.pop(x)
    return key

#recebe a mensagem e faz o que tem que ser feito
msg = input("Digite a frase para encripitar\nLembre-se de usar apenas carcteres minusculos da tabela ASCII\n>>> ")
msg = separa_silaba(msg)
key = gera_Key(7)
print('Chave = {}'.format(key))
ALFB = modifica_tabela(alf, key)
msg = encript(msg, ALFB)
print(msg)
msg = separa_silaba(msg)
msg = decript(msg, ALFB)
print(msg)
