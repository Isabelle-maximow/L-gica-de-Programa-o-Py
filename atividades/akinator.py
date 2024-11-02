print ("pense em um número de 0 a 10 e eu irei adivinhá-lo!")
n = input ("o número que voce pensou é par ou impar?: ")
if n == "Impar":
    n == input("O número que você está pensando é menor que 5?: ")
    if n == "sim":
       n == input("O número é maior que 1?: ")
       if n == "sim":
           input("Então, este numero é 3!")
       else:
            input("Então este numero é 1!")
    elif n == "não":
       n == input("O número é menor que 8?: ")
       if n == "não":
          input("Este numero é 9!")
       elif n == "sim":
           n == input("O número que você está pensando é maior que 5?: ") 
           if n == "sim":
               input("Então este numero é 7!")
           else:
               input("então este numero é 5!")
elif n == "par":
    n == input("O número que você está pensando é maior que 4?: ")
    if n == "sim":
        n == input("O número que você está pensando é maior que 6?: ")
        if n == "sim":
            input("Então este numero é 8!")
        else:
            input("Então este numero é 6!")
    if n == "não":
        n == input("O número que você está pensando é maior que 2?: ")
        if n == "sim":
            input("Então este numero é 4!")
        elif n == "não":
            n == input("o numero que está pensando é menor que 1?: ")
            if n == "sim":
                input("Então este numero é 0!")
            else:
                input("Então este numero é 2!")
else:
    input("resposta inválida")


               
           
        


