from controller_alunos import ControllerAlunos

def exibir_menu():
    print("\n1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Atualizar Aluno")
    print("4. Remover Aluno")
    print("5. Sair")

def main():
    controller = ControllerAlunos()
    opcoes = {
        '1': controller.criarAluno,
        '2': controller.listarAlunos,
        '3': controller.atualizarAluno,
        '4': controller.deletarAluno
    }
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ").strip()
        if opcao == '5':
            print("Saindo...")
            break
        
        acao = opcoes.get(opcao)
        if acao:
            acao()
            
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
