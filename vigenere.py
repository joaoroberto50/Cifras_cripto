from lib.caracteres import *
from random import choice
import sys

ALFB = ascii()

def msg_chave(msg, chave):
    if len(chave) < len(msg):
        aux = ''
        cont = 0
        for i in range(0, len(msg)):
            aux+=chave[cont]
            cont+=1
            if cont == len(chave):
                cont = 0
        chave = aux
    if len(chave) > len(msg):
        x = len(chave) - len(msg)
        for i in range(0, x):
            chave=chave[:-1]
    if len(chave) == len(msg):
        return chave

def encript(msg, chave, ALFB):
    cifra = ''
    chave = msg_chave(msg, chave)
    for i in range(0, len(msg)):
        x = ALFB.index(msg[i])
        y = ALFB.index(chave[i])
        x+=y
        if (x >= len(ALFB)):
            x -= len(ALFB)
        x = ALFB[x]
        cifra+=x
    return cifra

def decript(cifra, chave, ALFB):
    msg = ''
    chave = msg_chave(cifra, chave)
    for i in range(0, len(cifra)):
        x = ALFB.index(cifra[i])
        y = ALFB.index(chave[i])
        x -= y
        if (x < 0):
            x += len(ALFB)
        x = ALFB[x]
        msg+=x
    return msg

def gera_chave(msg, d = 1):
    if d == 1:
        key = ''
        alf_key = ascii()
        alf_key.pop()
        for i in range(0, len(msg)):
            key+= choice(alf_key)
    else:
        key = ''
        alf_key = ascii()
        for i in range(0, d):
            key += choice(alf_key)
    return key

def openFile(argv):
    try:
        arq = open(argv, 'r')
        msg = arq.read()
        arq.close()
        return msg
    except:
        return 1

def changeFile(argv, msg):
    arq = open(argv, 'w')
    arq.write(msg)
    arq.close()


if sys.argv[1] == '-e':
    msg = openFile(sys.argv[2])
    if(msg != 1):
        if len(sys.argv) == 4:
            key = gera_chave(msg, int(sys.argv[3]))
        else:
            key = gera_chave(msg)
        msg = encript(msg, key, ALFB)
        changeFile(sys.argv[2], msg)
        print('Guarde sua chave: {}'.format(key))
    else:
        print("ERRO: Arquivo nao existente")
elif sys.argv[1] == '-d':
    msg = openFile(sys.argv[2])
    if(msg != 1):
        key = input("Chave >>> ")
        msg = decript(msg, key, ALFB)
        changeFile(sys.argv[2], msg)
    else:
        print("ERRO: Arquivo nao existente")
elif sys.argv[1] == '-a':
    msg = input("Encript >>> ")
    key = input("Chave >>> ")
    msg = encript(msg, key, ALFB)
    print(msg)
    msg = decript(msg, key, ALFB)
    print(msg)
elif sys.argv[1] == '-h':
    print("CIFRA MONOALFABETICA\nComo usar:")
    print("-e para criptografar um arquivo .txt\npython vigenere.py -e <arquivo.txt>\nSe quiser gerara uma chave aleatoria insira o argumento com o tamanho da chave\n")
    print("-d para decriptografar um arquivo .txt\npython vigenere.py -d <arquivo.txt>\n")
    print("-a para usar de modo live\npython vigenere.py -a\n")
    print("AVISO: apenas usar espaco e carcters minuscolos validos ASCII")
else:
    print("{} nao e valido. Use -h".format(sys.argv[1]))

