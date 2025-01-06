from Funcionario import Funcionario
from Quarto import Quarto
from Reserva import Reserva

class Hotel:
  def __init__(self):
    self.funcionarios = []
    self.quartos = []
    self.reservas = []
    
  def cadastrar_funcionario(self, nome, funcao, salario):
    funcionario = Funcionario(nome, funcao, salario)
    self.funcionarios.append(funcionario)
    print(f"Funcionário {nome} cadastrado.")

  def listar_funcionarios(self):
    if self.funcionarios:
      for funcionario in self.funcionarios:
        print(funcionario)
    else:
      print("Nenhum funcionário cadastrado.")

  def cadastrar_quarto(self, numero, preco_diaria):
    quarto = Quarto(numero, preco_diaria)
    self.quartos.append(quarto)
    print(f"Quarto {numero} cadastrado.")

  def listar_quartos(self):
    if self.quartos:
      for quarto in self.quartos:
        print(quarto)
    else:
      print("Nenhum quarto cadastrado.")

  def alterar_status_quarto(self, numero, status):
    for quarto in self.quartos:
      if quarto.numero == numero:
        quarto.status = status
        print(f"Status do quarto {numero} alterado para {status}.")
        return
    print(f"Quarto {numero} não encontrado.")

  def cadastrar_reserva(self, nome_hospede, numero_quarto, dias_estadia):
    for quarto in self.quartos:
      if quarto.numero == numero_quarto and quarto.status == "disponível":
        reserva = Reserva(nome_hospede, numero_quarto, dias_estadia)
        self.reservas.append(reserva)
        quarto.status = "ocupado"
        print(f"Reserva realizada para {nome_hospede} no quarto {numero_quarto}.")
        return
    print("Quarto não disponível.")
  
  def calcular_conta(self, numero_quarto):
    for reserva in self.reservas:
      if reserva.numero_quarto == numero_quarto:
        for quarto in self.quartos:
          if quarto.numero == numero_quarto:
            conta = reserva.calcular_conta(quarto.preco_diaria)
            print(f"Conta final para o hóspede {reserva.nome_hospede}: R$ {conta:.2f}")
            return
    print(f"Reserva não encontrada para o quarto {numero_quarto}.")
