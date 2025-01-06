class Quarto:
    def __init__(self, numero, preco_diaria):
        self.numero = numero
        self.preco_diaria = preco_diaria
        self.status = "disponível" 
    
    def __str__(self):
        return f"Quarto {self.numero} - R$ {self.preco_diaria:.2f} - Status: {self.status}"
