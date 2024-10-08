
numbers = -1
sun = 0
count = 0

while numbers != 0:
  numbers = int(input("Informe o número: "))
  
  if numbers != 0:
    sun = sun + numbers
    count += 1
  
print(f"Quantidade de números digitados: {count}")
print(f"Soma total: {sun}")
print(f"Média artimética: {sun/count}")


