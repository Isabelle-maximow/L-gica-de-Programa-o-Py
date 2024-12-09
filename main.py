precos = {
    "camisetas": 35,
    "calças": 50,
    "regatas": 30,
    "shorts" : 45
}
As = "As"
while True:
    produto_procurado = input("Qual modelo deseja saber o preço?:  ")
    if produto_procurado == "shorts":
        As = "Os" 
    if produto_procurado in precos:
        print(f"{As} {produto_procurado} estão custando: {precos[produto_procurado]}R$")
        novamente = input("Gostaria de pesquisar outro produto?: ")
        if novamente != "sim":
            break

    else:
        cadastro = input("Opss! Não encontramos este produto. \n Deseja cadastrar o produto?: ")
        if cadastro == "sim":
            print("--" * 20)

            produto = input("Insira o nome do produto: ")
            precos[produto] = [input("Insira o valor do produto: ")]

            print("--" * 20)

            print("Valores cadastrados!")
            ver_estoque = input("Deseja ver o estoque?: ")
            print("--" * 20)

            if ver_estoque == "sim":
                for chave, valor in precos.items():             # mostra chave e valor juntos
                    print(f"{chave}: {valor}")
        else:
            excluir_produto = input("Deseja excluir algum produto do estoque?: ")
            if excluir_produto == "sim":
                print("--" * 20)
                produto = input("Insira o nome do produto que deseja remover: ")
                if produto in precos:
                    del precos[produto]
                    print("Produto excluido! \nLista atualizada.")
                    print("--" * 20)
                else:
                    ("Este produto não pertence ao estoque. ")
                print(f"{chave}: {valor}")




    