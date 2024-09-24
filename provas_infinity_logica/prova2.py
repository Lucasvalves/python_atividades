maximum_speed = float(input("Informe a velocidade do carro: "))
maximum_limit = 80

if maximum_speed > maximum_limit:
  fine_amount = 20 * (maximum_speed - maximum_limit)

  text_fine_amount = f"O valor da multa é de R$ {fine_amount:.2f}"
  text_fine_amount = text_fine_amount.replace('.', ",")

  print(f"Você foi multado. {text_fine_amount}")
