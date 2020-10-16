<<<<<<< HEAD
# Entrada da chave para criptografia e a frase a ser encriptada
# As duas são transformadas em maiúsculo pela função upper()
chave_entrada = input("Informa a chave: ").upper()
frase_entrada = input("Digite uma frase: ").upper()

# Vetores para armazenar os dados passados nas variáveis de entrada
frase = []
chave = []

# Os laços for irão separar caractere a caractere e armazenar nos vetores acima
# Armazena caracteres da frase
for i in range(len(frase_entrada)):
    # O código trabalha com caracteres maiúsculos, que possuem um valor de 65 a 90, dessa forma ignorando os espaços e outros caracteres
    if ord(frase_entrada[i])>90 or ord(frase_entrada[i])<65: 
        continue
    else:
        frase.append(frase_entrada[i])

# Armazena caracteres da chave
for i in range(len(chave_entrada)):
    chave.append(chave_entrada[i])

# Declaração de variáveis com os tamanhos de "chave" e "frase"
tam_chave = len(chave)
tam_frase = len(frase)

# Calculo para saber o tamanho da matriz que irá armazenar cada caractere
tam = (tam_chave*tam_chave) - tam_chave - tam_frase

while tam < 0:
    tam+= tam_chave

# Preenche a matriz com X caso sobrem espaços. Tornando uma matriz NxN
if tam > 0:
    for i in range(tam):
        frase.append('W')

# Declaração de variáveis auxiliares 
cont = 0
aux = 0

matriz = [chave]

# Criando a matriz e preenchendo com a chave e frase
while aux < len(frase):
    linha = []
    for j in range(len(chave)):
        linha.append(frase[j + cont])
        aux+= 1
    cont+= len(chave)
    matriz.append(linha)

##for i in range(len(matriz)):
##    print(matriz[i])

# Declaração de variáveis auxiliares    
confere = 999
index = 0

cifrado = []

# For p/ criptografar a mensagem. Foi usada uma transposição de colunas.
for j in range(tam_chave):
    for h in range(tam_chave):
        if matriz[0][h] == None:
            continue
        if ord(matriz[0][h]) < confere:
            confere = ord(matriz[0][h])
            index = h
    matriz[0][index] = None
    confere = 999
    for i in range(1,len(matriz)):
        cifrado.append(matriz[i][index])

aux_2 = 1
conjunto = len(cifrado)//len(chave)

# For p/ printar a mensagem crifrada de forma organizada, separando conjuntos de caracteres concatenados com o tamanho da palavra chave-1
# Exemplo: palavra chave com tamanho 6, printa uma concatenação de caracteres de tamanho 5 
print((len(chave)*10)*'=','\n')
for k in range(len(cifrado)):
    if aux_2 == conjunto:
        print(cifrado[k], end = ' ')
        aux_2 = 1
    else:
        print(cifrado[k], end = '')
        aux_2+= 1
print('\n')
print((len(chave)*10)*'=')
=======
# Entrada da chave para criptografia e a frase a ser encriptada
# As duas são transformadas em maiúsculo pela função upper()
chave_entrada = input("Informa a chave: ").upper()
frase_entrada = input("Digite uma frase: ").upper()

# Vetores para armazenar os dados passados nas variáveis de entrada
frase = []
chave = []

# Os laços for irão separar caractere a caractere e armazenar nos vetores acima
# Armazena caracteres da frase
for i in range(len(frase_entrada)):
    # O código trabalha com caracteres maiúsculos, que possuem um valor de 65 a 90, dessa forma ignorando os espaços e outros caracteres
    if ord(frase_entrada[i])>90 or ord(frase_entrada[i])<65: 
        continue
    else:
        frase.append(frase_entrada[i])

# Armazena caracteres da chave
for i in range(len(chave_entrada)):
    chave.append(chave_entrada[i])

# Declaração de variáveis com os tamanhos de "chave" e "frase"
tam_chave = len(chave)
tam_frase = len(frase)

# Calculo para saber o tamanho da matriz que irá armazenar cada caractere
tam = (tam_chave*tam_chave) - tam_chave - tam_frase

while tam < 0:
    tam+= tam_chave

# Preenche a matriz com X caso sobrem espaços. Tornando uma matriz NxN
if tam > 0:
    for i in range(tam):
        frase.append('W')

# Declaração de variáveis auxiliares 
cont = 0
aux = 0

matriz = [chave]

# Criando a matriz e preenchendo com a chave e frase
while aux < len(frase):
    linha = []
    for j in range(len(chave)):
        linha.append(frase[j + cont])
        aux+= 1
    cont+= len(chave)
    matriz.append(linha)

##for i in range(len(matriz)):
##    print(matriz[i])

# Declaração de variáveis auxiliares    
confere = 999
index = 0

cifrado = []

# For p/ criptografar a mensagem. Foi usada uma transposição de colunas.
for j in range(tam_chave):
    for h in range(tam_chave):
        if matriz[0][h] == None:
            continue
        if ord(matriz[0][h]) < confere:
            confere = ord(matriz[0][h])
            index = h
    matriz[0][index] = None
    confere = 999
    for i in range(1,len(matriz)):
        cifrado.append(matriz[i][index])

aux_2 = 1
conjunto = len(cifrado)//len(chave)

# For p/ printar a mensagem crifrada de forma organizada, separando conjuntos de caracteres concatenados com o tamanho da palavra chave-1
# Exemplo: palavra chave com tamanho 6, printa uma concatenação de caracteres de tamanho 5 
print((len(chave)*10)*'=','\n')
for k in range(len(cifrado)):
    if aux_2 == conjunto:
        print(cifrado[k], end = ' ')
        aux_2 = 1
    else:
        print(cifrado[k], end = '')
        aux_2+= 1
print('\n')
print((len(chave)*10)*'=')

