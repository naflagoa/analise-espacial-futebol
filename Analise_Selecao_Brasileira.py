import json
import pandas as pd

# 1 - Simulação de Dados JSON (Evento de passes da Seleção Brasileira)
json_data = """
[
  {"id": 1, "jogador": "Vini Jr", "equipe": "Brasil", "tipo": "Passe", "subtipo": "Progressivo", "localizacao": [85, 80], "sob_pressao": true, "resultado": "Sucesso"},
  {"id": 2, "jogador": "Lucas Paquetá", "equipe": "Brasil", "tipo": "Passe", "subtipo": "Lateral", "localizacao": [50, 50], "sob_pressao": false, "resultado": "Sucesso"},
  {"id": 3, "jogador": "Rodrygo", "equipe": "Brasil", "tipo": "Passe", "subtipo": "Progressivo", "localizacao": [75, 20], "sob_pressao": true, "resultado": "Falha"},
  {"id": 4, "jogador": "Marquinhos", "equipe": "Brasil", "tipo": "Passe", "subtipo": "Progressivo", "localizacao": [30, 40], "sob_pressao": false, "resultado": "Sucesso"},
  {"id": 5, "jogador": "Casemiro", "equipe": "Brasil", "tipo": "Passe", "subtipo": "Progressivo", "localizacao": [45, 60], "sob_pressao": true, "resultado": "Sucesso"},
  {"id": 6, "jogador": "Neymar", "equipe": "Brasil", "tipo": "Passe", "subtipo": "Progressivo", "localizacao": [70, 50], "sob_pressao": true, "resultado": "Sucesso"},
  {"id": 7, "jogador": "Raphinha", "equipe": "Brasil", "tipo": "Passe", "subtipo": "Lateral", "localizacao": [65, 10], "sob_pressao": false, "resultado": "Falha"},
  {"id": 8, "jogador": "Alisson", "equipe": "Brasil", "tipo": "Passe", "subtipo": "Progressivo", "localizacao": [5, 50], "sob_pressao": true, "resultado": "Sucesso"},
  {"id": 9, "jogador": "Bruno Guimarães", "equipe": "Brasil", "tipo": "Passe", "subtipo": "Lateral", "localizacao": [55, 30], "sob_pressao": false, "resultado": "Sucesso"},
  {"id": 10, "jogador": "Eder Militão", "equipe": "Brasil", "tipo": "Passe", "subtipo": "Progressivo", "localizacao": [25, 70], "sob_pressao": true, "resultado": "Falha"},
  {"id": 11, "jogador": "Vini Jr", "equipe": "Brasil", "tipo": "Passe", "subtipo": "Lateral", "localizacao": [90, 85], "sob_pressao": true, "resultado": "Falha"},
  {"id": 12, "jogador": "Casemiro", "equipe": "Brasil", "tipo": "Passe", "subtipo": "Lateral", "localizacao": [40, 50], "sob_pressao": false, "resultado": "Sucesso"}
]
"""

# 2 - Transformando o JSON em dataframe
data = json.loads(json_data)
df = pd.DataFrame(data)

# 3 - Criação de KPI: Eficiência de Passes Progressivos sob Pressão
# (Ajustado para puxar as colunas e textos exatos em português)
df_sob_pressao = df[(df['sob_pressao'] == True) & (df['subtipo'] == 'Progressivo')]
total_passes = len(df_sob_pressao)
passes_sucesso = len(df_sob_pressao[df_sob_pressao['resultado'] == 'Sucesso'])

kpi_passes_pressao = (passes_sucesso / total_passes) * 100 if total_passes > 0 else 0

print("Análise de Scouting - Seleção Brasileira (Dados Semiestruturados)")
print("-" * 65)
print(df.to_string())
print("-" * 65)
print(f"KPI - Eficiência de Passes Progressivos sob Pressão: {kpi_passes_pressao:.1f}%")

# 4 - Salvando em um bloco de notas
with open("dados_para_powerbi.json", "w", encoding="utf-8") as arquivo:
    arquivo.write(json_data)

print("Sucesso: O arquivo 'dados_para_powerbi.json' foi criado e salvo")