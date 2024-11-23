# atvd 1


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

