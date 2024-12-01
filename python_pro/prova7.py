dados = {
    2021: {
        "Fazenda A": {"milho": 800, "soja": 200, "trigo": 150},
        "Fazenda B": {"milho": 80, "soja": 150, "trigo": 120},
        "Fazenda C": {"milho": 90, "soja": 180, "trigo": 140},
    },
    2022: {
        "Fazenda A": {"milho": 150, "soja": 220, "trigo": 160},
        "Fazenda B": {"milho": 85, "soja": 160, "trigo": 130},
        "Fazenda C": {"milho": 95, "soja": 190, "trigo": 150},
    },
    2023: {
        "Fazenda A": {"milho": 156, "soja": 240, "trigo": 170},
        "Fazenda B": {"milho": 90, "soja": 170, "trigo": 150},
        "Fazenda C": {"milho": 140, "soja": 245, "trigo": 160},
    },
}

totais_por_ano = {}

for ano, fazendas in dados.items():
  total = sum (
    sum(culturas.values()) for culturas in fazendas.values()
  )
  totais_por_ano[ano] = total


ano_max_producao = max(totais_por_ano, key=totais_por_ano.get)
ano_min_producao = min(totais_por_ano, key=(totais_por_ano.get))

print(f"Ano com maior produção: {ano_max_producao} ({totais_por_ano[ano_max_producao]})")
print(f"Ano com menor produção: {ano_min_producao} ({totais_por_ano[ano_min_producao]})")

totais_por_cultura = {}

for ano, fazendas in dados.items():
  for culturas in fazendas.values():
    for cultura, producao in culturas.items():
      totais_por_cultura[cultura] = totais_por_cultura.get(cultura, 0) + producao

cultura_max_producao  = max(totais_por_cultura, key=totais_por_cultura.get)
cultura_min_producao = min(totais_por_cultura, key=totais_por_cultura.get)

print(f"Cultura com maior produção: {cultura_max_producao} ({totais_por_cultura[cultura_max_producao]})")
print(f"Cultura com menor produção: {cultura_min_producao} ({totais_por_cultura[cultura_min_producao]})")


ano_escolhido = 2022

totais_por_fazenda = {
  fazenda: sum(culturas.values()) for fazenda, culturas in dados[ano_escolhido].items()
}


fazenda_max_producao = max(totais_por_fazenda, key=totais_por_fazenda.get)
fazenda_min_producao = min(totais_por_fazenda, key=totais_por_fazenda.get)

print(f"Fazenda com maior produção em {ano_escolhido}: {fazenda_max_producao} ({totais_por_fazenda[fazenda_max_producao]})")
print(f"Fazenda com menor produção em {ano_escolhido}: {fazenda_min_producao} ({totais_por_fazenda[fazenda_min_producao]})")