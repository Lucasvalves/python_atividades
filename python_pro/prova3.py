alunos_cadastrados = []
materias = ("Matemática", "Ciências", "História")

while True:
  aluno = {}
  nome = input('Informe o nome do aluno: ')
  idade =  int(input('Informe a idade do aluno: '))
  aluno['nome'] = nome 
  aluno['idade'] = idade

  notas = []
  for materia in range(0,3):
    nota = float(input(f'Informe a nota do aluno em {materias[materia]}: '))
    notas.append(nota)
  aluno['notas'] = notas
  alunos_cadastrados.append(aluno)

  flag = input('Deseja continuar inserindo alunos? (sim/não) ').strip().lower()
  if flag != 'sim':
    break

#print(alunos_cadastrados)
print('Lista de todos os alunos cadastrados')
test = 0
total_notas  = 0
melhor_media = 0
aluno_melhor_media = None
for aluno in alunos_cadastrados:

  nome = aluno['nome']
  idade = aluno['idade']
  print(f'Nome: {nome}')
  print(f'Idade: {idade}')

  for index, valor in enumerate(aluno['notas']):
    print (f'Nota em {materias[index]}: {valor} ')

  total_notas = sum(aluno['notas']) 
  media = total_notas / len(aluno['notas'])
  print(f"Média das notas é: {media:.2f}", )
  print()
  aluno['media'] = media

  if media > melhor_media:
    melhor_media = media
    aluno_melhor_media = aluno

    
if aluno_melhor_media:
  print(f'\nAluno com a melhor média:')
  print(f'Nome: {aluno_melhor_media["nome"]}')
  print(f'Média: {aluno_melhor_media["media"]:.2f}')        

  
