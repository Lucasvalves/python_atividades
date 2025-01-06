class Funcionario:
  def __init__(self, nome, funcao, salario):
   self.nome = nome
   self.funcao = funcao
   self.salario = salario 
  
  def __str__(self):
    return f"{self.nome} - {self.funcao} - R$ {self.salario:.2f}"