alunos = [ 
    ["Ana", "13", "turma A"],
    ["carlos", "15", "turma B"],
    ["Maria", "16", "turma C"],
    ["Nana", "13", "turma A"],
]


while True:
    print("Menu principal")
    print("\n 1 - Cadastrar Alunos")
    print(" 2 - Listar Alunos")
    print(" 3 - Excluir Alunos")
    print(" 4 - Listar alunos por turma")
    print(" 5 - Sair")

    resposta = int(input("O que deseja fazer?: "))
    
    if resposta == 1:                 # CADASTRAR ALUNO
        while True: 
            cadastro = input("Nome do aluno: ")
            cadastro_idade = int (input("Idade do aluno: "))
            cadastro_turma = input("Turma deste aluno: ")
            alunos.append({cadastro, cadastro_idade, cadastro_turma})
            print("Aluno cadastrado!")

            continuar = input("Deseja cadastrar mais um aluno?(sim ou não): ").lower
            if continuar != "sim":
                break

    elif resposta == 2:              # MOSTRAR LISTA
        print(f"{alunos[0]} | {alunos[1]} | {alunos[2]}")
        if alunos == []:
            print("Sem alunos.\n Cadastre no menu inicial ")

    elif resposta == 3:                             # REMOVER ALUNO
        deletado_turma = input("Insira a turma do aluno que deseja deletar: ").lower
        if deletado_turma in alunos:
            deletado_aluno = input("Insira o nome do aluno que deseja deletar: ").lower
            if deletado_aluno in alunos:
                certeza = input("Certeza que deseja deletar ete aluno?: ").lower
                if certeza == "sim":
                    alunos.remove(deletado_aluno)
                    print("Este aluno foi removido do sistema!")
                else: 
                    print("Aluno não removido!")  
            else:
                print("Aluno não encontrado")
        else:
            print("turma não encontrada!")
        
    elif resposta == 4:                                  # ANALISAR POR TURMA
        turma = str(input("Qual turma deseja analisar? ")).lower
        for aluno in alunos:
            turma = aluno[2]
            print(f"{aluno[2]}  | {aluno[2]} | {aluno[2]}")
    
    else:
        print("Até a próxima!")
        break
        






