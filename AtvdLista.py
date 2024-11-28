# atvd 1
"""

lista = []
n = 1
for i in range (5):
    num = int(input(f"adicione o {n} numero: "))
    n = n + 1 
    lista.append(num)
for i in lista:
    print(i, end=" - ")

  
# atvd 2 

lista = []
n = 1
for i in range (5):
    num = input(f"adicione o {n} numero: ")
    n = n + 1
    lista.append(num)
lista.reverse()
for i in lista:
    print(i, end= " - ")


# atvd 3 
lista = []
n = 1
for i in range (4):
    notas = float(input(f"adicione a nota {n}: "))
    n += 1
    lista.append(notas)
for i in lista:
    print(i, end= " - ")

soma = sum(lista)
media = soma / n
print(f" a média deste aluno foi: {media}")

"""

# atvd 4 
"""

lista = []
soma = 0
num = int(input("Informe o numero caracteres: "))
for i in range (0,num):
    caracteres = str(input(f"Insira o {i+1} caractere: ")).lower()
    lista.append(caracteres)
    if caracteres == "a" and caracteres == "e" and caracteres == "i" and caracteres == "o" and caracteres == "u":
        print("essa letra não é uma consoante")
    else:
        soma += 1
        print(f"a letra {caracteres} é uma consoante!")
print(f"O total de consoantes foi: {soma}")

"""

#atvd 5
"""

listapar = []
listaimpar = []
lista = []
num = int(input("Informe o numero caracteres: "))
for i in range (0,num):
    numeros = int(input(f"insira o {i+1} número: "))
    lista.append(numeros)
    if numeros % 2 == 0: #identificar numero par
        listapar.append(numeros)
    else:
        listaimpar.append(numeros)
print(f"Do conjunto {lista} os pares são {listapar} e os impares são {listaimpar}")

"""

# atvd 6 
vetor = []
n = 0
multi = 1                               # Declarar uma variavel com valor 1 ; add: multi *= num - para realizar a multiplicação
for i in range (4):
    num = int(input(f"Insira a {n + 1}° nota: "))
    n += 1
    multi *= num
    vetor.append(num)
soma = sum(vetor)

print(f"A soma desses numeros equivale a: {soma}, e a multiplicação: {multi}")

