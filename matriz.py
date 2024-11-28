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

print("vamos descobrir a média! ")
matriz = []
for i in range(6):
    notas = []
    aluno = input("Insira o nome do aluno: ")
    n = 0
    for i in range(4):
        nota = float(input(f"Insira a {n+1}ª nota do aluno {aluno}: "))
        notas.append(nota)
        if nota == str:
            print("por favor, insira somente numeros!")
        else:
            continue 
    soma = sum(notas)
    media = soma / 4
    matriz.append((aluno, notas, media))

print("\nResumo final:")
for aluno, notas, media in matriz:
    print(f"Aluno: {aluno} | Notas: {notas} | Média: {media:.2f}")

    



