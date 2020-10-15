from lib.caracteres import *
import sys

ALFB = ascii()
def encript(msg, chave, ALFB):
	cifra = ''
	for i in msg:
		x = ALFB.index(i)
		x+=chave
		if(x >= len(ALFB)):
			x-=len(ALFB)
		x = ALFB[x]
		cifra+=x
	return cifra

def decript(cifra, chave, ALFB):
	msg = ''
	for i in cifra:
		x = ALFB.index(i)
		x-=chave
		if(x < 0):
			x+=len(ALFB)
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
		msg = encript(msg, int(sys.argv[3]), ALFB)
		changeFile(sys.argv[2], msg)
	else:
		print("ERRO: Arquivo nao existente")
elif sys.argv[1] == '-d':
	msg = openFile(sys.argv[2])
	if(msg != 1):
		msg = decript(msg, int(sys.argv[3]), ALFB)
		changeFile(sys.argv[2], msg)
	else:
		print("ERRO: Arquivo nao existente")
elif sys.argv[1] == '-a':
	msg = input("Encript >>> ")
	chave = int(input("Chave >>> "))
	msg = encript(msg, chave, ALFB)
	print(msg)
	msg = decript(msg, chave, ALFB)
	print(msg)
elif sys.argv[1] == '-h':
	print("CIFRA DE CESAR\nComo usar:")
	print("-e para criptografar um arquivo .txt\npython cesar_cif.py -e <arquivo.txt> <chave>\n")
	print("-d para decriptografar um arquivo .txt\npython cesar_cif.py -d <arquivo.txt> <chave>\n")
	print("-a para usar de modo live\npython cesar_cif.py -a\n")
	print("AVISO: apenas usar carcters validos ASCII")
else:
	print("{} nao e valido. Use -h".format(sys.argv[1]))
