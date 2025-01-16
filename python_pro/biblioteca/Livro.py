class Livro:
    def __init__(self, titulo, autor, id):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.status_de_emprestimo = "disponível"

    def __str__(self):
        return f"Livro: {self.titulo}, Autor: {self.autor}, ID: {self.id}, Status: {self.status_de_emprestimo}"