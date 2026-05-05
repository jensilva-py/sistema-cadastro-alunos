# Sistema de Cadastro de Alunos

alunos = []

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade: "))
    curso = input("Digite o curso: ")

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso
    }

    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!\n")


def listar_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.\n")
    else:
        print("\nLista de Alunos:")
        for i, aluno in enumerate(alunos):
            print(f"{i+1}. {aluno['nome']} - {aluno['idade']} anos - {aluno['curso']}")
        print()


def menu():
    while True:
        print("=== SISTEMA DE CADASTRO ===")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!\n")


menu()
