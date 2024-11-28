# INTRODUÇÃO
""" matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(f" o tamanho da matrix é: {len(matriz)}") #le o tamanho dela, no caso 3. 3x3
print(matriz[0] [0]) # linha e coluna 
print(matriz[1] [2]) """

# PERCORRER A MATRIZ 
""" matriz =  [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print("matriz: ")
for i in range (len(matriz)):
    print(matriz [i]) """
"""
matriz =  [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print("matriz: ")
for i in range (len(matriz)): #PERCORRE AS LINHAS = i
    print(matriz[i])
    for j in range (len(matriz[i])): #PERCORE AS COLUNAS = j  
        print(f"Elemento [{i}] [{j}] = {matriz [i] [j]}")


# USUARIO CRIAR MATRIZ 3X3

matriz = []
print("Preencha uma matrix 3x3: ")
for i in range (3):
    linha = [] #cd linha da matriz 
    for coluna in range (3):
        valor = int(input(f"Digite um valor para a posição [{i}]X[{coluna}]"))
        linha.append(valor) # guardando o valor na linha !!
    matriz.append(linha)
for linha in matriz:
    print(linha)
"""
#atvd 1
# 6x4
matriz = []
notas = []                           
for i in range (6):
    linhas = []
    soma = 0
    n = 0
    qtd = 0
    aluno = input("insira o nome do aluno: ")
    for colunas in range (4):
        nota = float(input(f"Insira a {n + 1}° nota do aluno {aluno}: "))  
        qtd += 1
        n + 1
        linhas.append(notas)
    media = sum(linhas) / qtd
    matriz.append(linhas)


