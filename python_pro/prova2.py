equipes = [
  ('Furação', [7.1, 8.0, 9.5]), 
  ('Tsunâmi', [7.0, 8.1, 9.7]), 
  ('Galaticos', [8.0, 7.1, 9.9]),
  ('Avante', [7.2, 9.5, 9.3]),
  ('Estronda', [7.0, 9.1, 9.8])
]
media = 0
lista_de_medias = []

for equipe, pontuacoes in equipes:
  media = sum(pontuacoes) / len(pontuacoes)
  lista_de_medias.append((equipe, media))
  

lista_de_medias.sort(key=lambda x: x[1], reverse=True) 

classificacao = lista_de_medias

print("Classificação de equipes")
for equipe, media in classificacao:
  print(f"Equipe {equipe} {media:.2f}")