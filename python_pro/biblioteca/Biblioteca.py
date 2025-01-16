from Livro import Livro
from Membro import Membro

class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.membros = []

    def cadastrar_livro(self, titulo, autor, id):
        livro = Livro(titulo, autor, id)
        self.catalogo.append(livro)
        print(f"Livro '{titulo}' cadastrado com sucesso!")

    def listar_livros(self):
        if not self.catalogo:
            print("Nenhum livro cadastrado.")
        else:
            for livro in self.catalogo:
                print(livro)

    def cadastrar_membro(self, nome, numero_membro):
        membro = Membro(nome, numero_membro)
        self.membros.append(membro)
        print(f"Membro '{nome}' cadastrado com sucesso!")

    def listar_membros(self):
        if not self.membros:
            print("Nenhum membro cadastrado.")
        else:
            for membro in self.membros:
                print(membro)

    def emprestar_livro(self, id, numero_membro):
        livro = next((livro for livro in self.catalogo if livro.id == id), None)
        membro = next((membro for membro in self.membros if membro.numero_membro == numero_membro), None)

        if not livro:
            print("Livro não encontrado.")
        elif not membro:
            print("Membro não encontrado.")
        elif livro.status_de_emprestimo == "emprestado":
            print(f"O livro '{livro.titulo}' já está emprestado.")
        else:
            livro.status_de_emprestimo = "emprestado"
            membro.historico_emprestimos.append(livro.titulo)
            print(f"O livro '{livro.titulo}' foi emprestado para o membro '{membro.nome}'.")

    def devolver_livro(self, id):
        livro = next((livro for livro in self.catalogo if livro.id == id), None)

        if not livro:
            print("Livro não encontrado.")
        elif livro.status_de_emprestimo == "disponível":
            print(f"O livro '{livro.titulo}' já está disponível.")
        else:
            livro.status_de_emprestimo = "disponível"
            print(f"O livro '{livro.titulo}' foi devolvido com sucesso.")

    def pesquisar_livro(self, termo):
        resultados = [livro for livro in self.catalogo if termo.lower() in livro.titulo.lower() or termo.lower() in livro.autor.lower()]
        if not resultados:
            print("Nenhum livro encontrado.")
        else:
            for livro in resultados:
                print(livro)
