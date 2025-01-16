from Biblioteca import Biblioteca

def menu():
    print("\nMenu da Biblioteca Infinity:")
    print("1. Cadastrar Livro")
    print("2. Listar Livros")
    print("3. Cadastrar Membro")
    print("4. Listar Membros")
    print("5. Emprestar Livro")
    print("6. Devolver Livro")
    print("7. Pesquisar Livro")
    print("8. Sair")
    return input("Escolha uma opção: ")

def main():
    biblioteca = Biblioteca()

    while True:
        opcao = menu()
        if opcao == "1":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            id = input("ID do livro: ")
            biblioteca.cadastrar_livro(titulo, autor, id)
        elif opcao == "2":
            biblioteca.listar_livros()
        elif opcao == "3":
            nome = input("Nome do membro: ")
            numero_membro = input("Número do membro: ")
            biblioteca.cadastrar_membro(nome, numero_membro)
        elif opcao == "4":
            biblioteca.listar_membros()
        elif opcao == "5":
            id = input("ID do livro: ")
            numero_membro = input("Número do membro: ")
            biblioteca.emprestar_livro(id, numero_membro)
        elif opcao == "6":
            id = input("ID do livro: ")
            biblioteca.devolver_livro(id)
        elif opcao == "7":
            termo = input("Digite o título ou autor para pesquisar: ")
            biblioteca.pesquisar_livro(termo)
        elif opcao == "8":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
