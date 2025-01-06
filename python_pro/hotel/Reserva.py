class Reserva:
  def __init__(self, nome_hospede, numero_quarto, dias_estadia):
    self.nome_hospede = nome_hospede
    self.numero_quarto = numero_quarto
    self.dias_estadia = dias_estadia

  def calcular_conta(self, preco_diaria):
    return self.dias_estadia * preco_diaria