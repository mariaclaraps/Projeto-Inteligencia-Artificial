import pandas as pd

# 1. Carregar o dataset
dataset_path = "data/CovidData.csv"  # Caminho do arquivo
df = pd.read_csv(dataset_path)  # Lendo o CSV

# 2. Visualizar as primeiras linhas do dataset
print("Visualizando os dados:\n", df.head())

# 3. Verificar estatísticas básicas do dataset
print("\nResumo estatístico:\n", df.describe())
