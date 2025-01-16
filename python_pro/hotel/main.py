from Hotel import Hotel 

def menu():
  hotel = Hotel()
  while True:
    print("\nHotel Infinity")
    opcao = input("Escolha uma opção: \n1 - Cadastrar Funcionário\n2 - Cadastrar Quarto\n3 - Realizar Reserva\n4 - Alterar Status do Quarto\n5 - Calcular Conta Final\n6 - Listar Funcionários\n7 - Listar Quartos\n8 - Sair\n")

    if opcao == "1":
      nome = input("Nome do funcionário: ")
      funcao = input("Função do funcionário: ")
      salario = float(input("Salário do funcionário: "))
      hotel.cadastrar_funcionario(nome, funcao, salario)
  
    elif opcao == "2":
      numero = int(input("Número do quarto: "))
      preco = float(input("Preço por diária: R$ "))
      hotel.cadastrar_quarto(numero, preco)
  
    elif opcao == "3":
      nome_hospede = input("Nome do hóspede: ")
      numero_quarto = int(input("Número do quarto: "))
      dias_estadia = int(input("Número de dias de estadia: "))
      hotel.cadastrar_reserva(nome_hospede, numero_quarto, dias_estadia)
  
    elif opcao == "4":
      numero = int(input("Número do quarto: "))
      status = input("Novo status (disponível/ocupado): ")
      hotel.alterar_status_quarto(numero, status)
  
    elif opcao == "5":
      numero_quarto = int(input("Número do quarto: "))
      hotel.calcular_conta(numero_quarto)
  
    elif opcao == "6":
      hotel.listar_funcionarios()
    
    elif opcao == "7":
      hotel.listar_quartos()
    
    elif opcao == "8":
      print("Saindo...")
      break

    else:
      print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
  menu()
