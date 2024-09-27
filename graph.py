import matplotlib.pyplot as plt
import pandas as pd

# Limpeza dos dados e renomeação das colunas

data = pd.read_csv('dados.csv', sep=',', encoding='utf-8', header=None)
data_clean = data.drop([0, 1]).reset_index(drop=True)
data_clean.columns = ['Apresentador', 'Data', 'Título do Artigo', 'Ano de Publicação', 'Eixo Temático', 
                      'Link do Artigo', 'Status', 'TCC', 'PIBIC']

# Convertendo colunas relevantes para os tipos corretos
data_clean['Ano de Publicação'] = pd.to_numeric(data_clean['Ano de Publicação'], errors='coerce')
data_clean['Data'] = pd.to_datetime(data_clean['Data'], format='%d/%m/%Y', errors='coerce')

# 1. Distribuição dos eixos temáticos
eixos_tematicos = data_clean['Eixo Temático'].value_counts()

# 2. Distribuição por ano de publicação
anos_publicacao = data_clean['Ano de Publicação'].dropna().value_counts().sort_index()

# 3. Número de apresentações ao longo do tempo
apresentacoes_por_data = data_clean['Data'].dropna().value_counts().sort_index()

def plot_eixos_tematicos():
    plt.figure(figsize=(10, 5))
    plt.bar(eixos_tematicos.index, eixos_tematicos.values, color='skyblue')
    plt.title('Distribuição dos Eixos Temáticos')
    plt.xlabel('Eixo Temático')
    plt.ylabel('Número de Apresentações')
    plt.xticks(rotation=85)
    plt.tight_layout()
    plt.show()

def plot_anos_publicacao():
    plt.figure(figsize=(10, 5))
    plt.bar(anos_publicacao.index, anos_publicacao.values, color='lightgreen')
    plt.title('Distribuição por Ano de Publicação')
    plt.xlabel('Ano de Publicação')
    plt.ylabel('Número de Artigos')
    plt.tight_layout()
    plt.show()

def plot_apresentacoes_por_data():
    plt.figure(figsize=(10, 5))
    plt.plot(apresentacoes_por_data.index, apresentacoes_por_data.values, marker='o', color='salmon')
    plt.title('Número de Apresentações ao Longo do Tempo')
    plt.xlabel('Data')
    plt.ylabel('Número de Apresentações')
    plt.tight_layout()
    plt.show()

# Chamar as funções para gerar os gráficos
plot_eixos_tematicos()
plot_anos_publicacao()
plot_apresentacoes_por_data()