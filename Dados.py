import pandas as pd
import numpy as np

# Passo 1: Ler o arquivo CSV
df = pd.read_csv('dados.csv', sep=';', engine='python')

# Passo 2: Corrigir possíveis erros nos dados

# 2.1 Remover aspas simples das datas
df['Date'] = df['Date'].astype(str).str.replace("'", "")

# 2.2 Corrigir valores não numéricos na coluna 'Calories'
df['Calories'] = df['Calories'].astype(str).str.extract(r'(\d+)')  # Extrai apenas os números
df['Calories'] = pd.to_numeric(df['Calories'], errors='coerce')    # Converte para número

# 2.3 Corrigir formato incorreto de datas (como '20201226')
df['Date'] = df['Date'].replace('20201226', '2020/12/26')

# 2.4 Substituir valores ausentes em 'Calories' por 0
df['Calories'] = df['Calories'].fillna(0)

# 2.5 Substituir valores ausentes em 'Date' por uma data padrão
df['Date'] = df['Date'].fillna('1900/01/01')

# 2.6 Converter coluna 'Date' para datetime
df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d', errors='coerce')

# 2.7 Remover linhas com valores nulos restantes (por exemplo, se a data ainda for inválida)
df = df.dropna()

# 2.8 Corrigir possíveis IDs duplicados (opcional: resetar o índice ou remover duplicatas)
df = df.drop_duplicates(subset='ID')

# Mostrando resultados
print("\n✅ DataFrame final após limpeza:")
print(df)

print("\n📋 Informações finais do DataFrame limpo:")
print(df.info())
