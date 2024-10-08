number = int(input("informe um número de 1 a 10: ")) 

if number > 10:
  print(f"Número invalido. por favor informe um número de 1 a 10")
  
print(f"Tabuada de {number}: ")
for i in range(1,11):
  print(f"{number} X {i} = {number * i}")