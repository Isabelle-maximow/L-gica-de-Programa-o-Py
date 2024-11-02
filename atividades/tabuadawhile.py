num = int(input("insira o numero que vc deseja treinar a tabuada: "))
contador = 0
acertos = 0
erros = 0

while True:
    resposta_usuario = int(input(f"{num} x {contador} = "))
    resultado_correto = num * contador
    if resposta_usuario == resultado_correto:
        print("CORRETO")
        acertos += 1
        contador += 1
    else:
        print(f"QUE PENA, VOCÊ ERROU, O VALOR CORRETO É {resultado_correto}")
        erros += 1
        contador += 1

    if contador >= 11:  # p parar quando tibver x10
            break

print(f"Total de acertos: {acertos}")
print(f"Total de erros: {erros}")
repetir = input("Deseja começar de novo? (s/n): ").strip().lower()
if repetir != 's':
    print("Obrigado por jogar!")  #arrumar loop caso escolha sim 