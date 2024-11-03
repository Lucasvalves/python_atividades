def soma(a,b):
  return a+b
def sub(a,b):
  return a-b
def mult(a,b):
  return a*b
def div(a,b):
  return a/b

while(True):
  operacao = input('Qual operação ele deseja realizar? (+ - * /): ')
  primeiro_numero = int(input('Informe o primeiro número: '))
  segundo_numero = int(input('Informe o segundo número: '))

  if operacao == '+': print(soma(primeiro_numero, segundo_numero))
  if operacao == '-': print(sub(primeiro_numero, segundo_numero))
  if operacao == '*': print(mult(primeiro_numero, segundo_numero))
  if operacao == '/': 
    if segundo_numero == 0:
      input('Opreação invalida. Digite um número maior que 0 ')
      primeiro_numero = int(input('Informe o primeiro número: '))
      segundo_numero = int(input('Informe o segundo número: '))

    print(div(primeiro_numero, segundo_numero))

  continuar = input('Deseja sair? sim/não: ').strip().lower()

  if continuar != 'sim':
    break
