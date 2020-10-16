# Discentes: João Roberto & Claudionor Amâncio
# Importação de arquivo caracteres.py, que foi criado e está na pasta lib;
# e importação da biblioteca sys
from lib.caracteres import *
import sys

#Declaração de variáveis. ALFB é uma tabela que aceita os caracteres em minúsculo
#transformados pela função lower_case().
ALFB = lower_case()
BFLA = []
temp = simbols()

#Preenche a tabela BFLA com a função simbols que recebe os simbolos da tabela ALFB
for i in range(0, 28):
    BFLA.append(temp[i])

#Busca o indice do caractere da mensagem na tabela ALBF e altera pelo caractere
#que esta na mesma posição na tabela BLFA
def encript(msg, ALFB, BFLA):
    code = ''
    for i in msg:
        x = ALFB.index(i)
        x = BFLA[x]
        code+=x
    return code

#Realiza a operação contrária da função de encriptação.
def decript(code, ALFB, BFLA):
    msg = ''
    for i in code:
        x = BFLA.index(i)
        x = ALFB[x]
        msg+=x
    return msg

# Função para abrir o arquivo .txt
def openFile(argv):
    try:
        arq = open(argv, 'r')
        msg = arq.read()
        arq.close()
        return msg
    except:
        return 1

# Função para alteração do arquivo .txt
def changeFile(argv, msg):
        arq = open(argv, 'w')
        arq.write(msg)
        arq.close()

# Declaração dos argumentos por linha da comando para:
# Encriptação
if sys.argv[1] == '-e':
    msg = openFile(sys.argv[2])
    if(msg != 1):
        msg = encript(msg, ALFB, BFLA)
        changeFile(sys.argv[2], msg)
    else:
        print("ERRO: Arquivo nao existente")
# Decriptação
elif sys.argv[1] == '-d':
    msg = openFile(sys.argv[2])
    if(msg != 1):
        msg = decript(msg, ALFB, BFLA)
        changeFile(sys.argv[2], msg)
    else:
        print("ERRO: Arquivo nao existente")
# Modo de interação
elif sys.argv[1] == '-a':
    msg = input("Encript >>> ")
    msg = encript(msg, ALFB, BFLA)
    print(msg)
    msg = decript(msg, ALFB, BFLA)
    print(msg)
# Comando para ajuda
elif sys.argv[1] == '-h':
    print("CIFRA MONOALFABETICA\nComo usar:")
    print("-e para criptografar um arquivo .txt\npython monoalfabeica.py -e <arquivo.txt>\n")
    print("-d para decriptografar um arquivo .txt\npython monoalfabeica.py -d <arquivo.txt>\n")
    print("-a para usar de modo live\npython monoalfabeica.py -a\n")
    print("AVISO: apenas usar espaco e carcters minuscolos validos ASCII")
else:
    print("{} nao e valido. Use -h".format(sys.argv[1]))
