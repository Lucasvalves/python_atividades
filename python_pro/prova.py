
produto = ''
preco = 0.0
continuar = ''

total_gasto = 0
produto_mais_barato = ''
preco_mais_barato =  float('inf')
qtd_produto_maior_mil = 0

while True:
  produto = input("Informe o nome do produto: ")

  preco = float(input("Informe o preço do produto: "))


  total_gasto += preco

  if preco > 1000:
    qtd_produto_maior_mil+=1
    
  if  preco > preco_mais_barato:
    preco_mais_barato = preco
    produto_mais_barato = produto  

  continuar = input("Deseja inserir mais produtos (sim/não): ").strip().lower()
  if continuar != 'sim':
    break

print(f"Total gasto na compra: R${total_gasto:.2f}")
print(f"Quantidade de produtos que custam mais de R$1000: {qtd_produto_maior_mil}")
print(f"Nome do produto mais barato: {produto_mais_barato}")