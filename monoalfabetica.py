from lib.caracteres import *
import sys

ALFB = lower_case()
BFLA = []
temp = simbols()

for i in range(0, 28):
    BFLA.append(temp[i])

def encript(msg, ALFB, BFLA):
    code = ''
    for i in msg:
        x = ALFB.index(i)
        x = BFLA[x]
        code+=x
    return code

def decript(code, ALFB, BFLA):
    msg = ''
    for i in code:
        x = BFLA.index(i)
        x = ALFB[x]
        msg+=x
    return msg

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
        msg = encript(msg, ALFB, BFLA)
        changeFile(sys.argv[2], msg)
    else:
        print("ERRO: Arquivo nao existente")
elif sys.argv[1] == '-d':
    msg = openFile(sys.argv[2])
    if(msg != 1):
        msg = decript(msg, ALFB, BFLA)
        changeFile(sys.argv[2], msg)
    else:
        print("ERRO: Arquivo nao existente")
elif sys.argv[1] == '-a':
    msg = input("Encript >>> ")
    msg = encript(msg, ALFB, BFLA)
    print(msg)
    msg = decript(msg, ALFB, BFLA)
    print(msg)
elif sys.argv[1] == '-h':
    print("CIFRA MONOALFABETICA\nComo usar:")
    print("-e para criptografar um arquivo .txt\npython monoalfabeica.py -e <arquivo.txt>\n")
    print("-d para decriptografar um arquivo .txt\npython monoalfabeica.py -d <arquivo.txt>\n")
    print("-a para usar de modo live\npython monoalfabeica.py -a\n")
    print("AVISO: apenas usar espaco e carcters minuscolos validos ASCII")
else:
    print("{} nao e valido. Use -h".format(sys.argv[1]))
