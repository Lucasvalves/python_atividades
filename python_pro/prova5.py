

def processador_texto(texto, **kwargs):

  contar_palavras = lambda t: len(t.split())

  contar_letras = lambda t: len(t.replace(" ", ""))

  inverter_texto = lambda t: t[:: -1]

  substituir_palavra = lambda t, antiga, nova: t.replace(antiga, nova)

  for operacao, valor in kwargs.items():
    if operacao == "contar_palavras":
        print(f"Número de palavras: {contar_palavras(texto)}")
    elif operacao == "contar_letras":
        print(f"Número de letras: {contar_letras(texto)}")
    elif operacao == "inverter_texto":
      print(f"Texto invertido: {inverter_texto(texto)}")
    elif operacao == "substituir_palavra" and isinstance(valor, dict):
      antiga = valor.get('antiga', '')
      nova = valor.get('nova', '')
      texto = substituir_palavra(texto, antiga, nova)
      print(f'Texto depois da substituição: {texto}')
    else: 
      print(f"Operação invalida: {operacao}")

  return texto

texto_inicial = "Python é uma linguagem de programação facil de aprender"

resultado = processador_texto(texto_inicial, contar_palavras=True, contar_letras=True, inverter_texto=True, substituir_palavra = {"antiga": "facil", "nova": "tranquila"})

print("\nTexto final: ",resultado)