class Membro:
    def __init__(self, nome, numero_membro):
        self.nome = nome
        self.numero_membro = numero_membro
        self.historico_emprestimos = []

    def __str__(self):
        return f"Membro: {self.nome}, Número: {self.numero_membro}, Histórico: {', '.join(self.historico_emprestimos) if self.historico_emprestimos else 'Nenhum'}"