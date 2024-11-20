biblioteca = []
emprestimos = {}

def adicionar_livro(titulo, autor, copias):
    biblioteca.append({"titulo": titulo, "autor": autor, "copias": copias})
    print(f'Livro "{titulo}" adicionado com sucesso!')

def listar_livros():
    if biblioteca:
        print("\nLista de Livros Disponíveis:")
        for livro in biblioteca:
            print(f'Título: {livro["titulo"]}, Autor: {livro["autor"]}, Cópias disponíveis: {livro["copias"]}')
    else:
        print("\nNenhum livro disponível na biblioteca.")

def emprestar_livro(titulo, usuario):
    for livro in biblioteca:
        if livro["titulo"].lower() == titulo.lower():
            if livro["copias"] > 0:
                livro["copias"] -= 1
                if usuario not in emprestimos:
                    emprestimos[usuario] = []
                emprestimos[usuario].append(titulo)
                print(f'Livro "{titulo}" emprestado para {usuario}.')
                return
            else:
                print(f'O livro "{titulo}" não está disponível no momento.')
                return
    print(f'O livro "{titulo}" não foi encontrado na biblioteca.')

def devolver_livro(titulo, usuario):
    if usuario in emprestimos and titulo in emprestimos[usuario]:
        for livro in biblioteca:
            if livro["titulo"].lower() == titulo.lower():
                livro["copias"] += 1
                emprestimos[usuario].remove(titulo)
                print(f'Livro "{titulo}" devolvido por {usuario}.')
                return
    print(f'O livro "{titulo}" não foi encontrado nos empréstimos de {usuario}.')

def verificar_disponibilidade(titulo):
    for livro in biblioteca:
        if livro["titulo"].lower() == titulo.lower():
            if livro["copias"] > 0:
                print(f'O livro "{titulo}" está disponível ({livro["copias"]} cópias).')
            else:
                print(f'O livro "{titulo}" não está disponível no momento.')
            return
    print(f'O livro "{titulo}" não foi encontrado na biblioteca.')

def mostrar_livros_emprestados(usuario):
    if usuario in emprestimos and emprestimos[usuario]:
        print(f'\nLivros emprestados por {usuario}:')
        for titulo in emprestimos[usuario]:
            print(f'- {titulo}')
    else:
        print(f'\n{usuario} não possui livros emprestados.')

while True:
    print("\nSistema de Gerenciamento da Biblioteca")
    print("1. Adicionar Livro")
    print("2. Listar Livros Disponíveis")
    print("3. Empréstimo de Livro")
    print("4. Devolução de Livro")
    print("5. Verificar Disponibilidade de Livro")
    print("6. Mostrar Livros Emprestados")
    print("7. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título do livro: ")
        autor = input("Autor do livro: ")
        copias = int(input("Número de cópias disponíveis: "))
        adicionar_livro(titulo, autor, copias)
    elif opcao == "2":
        listar_livros()
    elif opcao == "3":
        titulo = input("Título do livro a emprestar: ")
        usuario = input("Nome do usuário: ")
        emprestar_livro(titulo, usuario)
    elif opcao == "4":
        titulo = input("Título do livro a devolver: ")
        usuario = input("Nome do usuário: ")
        devolver_livro(titulo, usuario)
    elif opcao == "5":
        titulo = input("Título do livro para verificar: ")
        verificar_disponibilidade(titulo)
    elif opcao == "6":
        usuario = input("Nome do usuário: ")
        mostrar_livros_emprestados(usuario)
    elif opcao == "7":
        print("Finalizando o programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
