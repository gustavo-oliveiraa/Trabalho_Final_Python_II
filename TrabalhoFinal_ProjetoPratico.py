import pandas as pd
import folium
import matplotlib.pyplot as plt

# 1. Tratamento e Limpeza da Base de Dados

df = pd.read_csv('DF.csv', sep=';', low_memory=False)

df_gama = df[df['DSC_LOCALIDADE'].str.upper().isin(['GAMA', 'GAMA LESTE', 'GAMA NORTE'])]

mask_positivo = df_gama['DSC_ESTABELECIMENTO'].str.upper().str.contains('SALAO|SALÃO|BELEZA', na=False)

mask_negativo = df_gama['DSC_ESTABELECIMENTO'].str.upper().str.contains('FESTA|DANÇA|TESTEMUNHAS|IGREJA', na=False)

df_salao = df_gama[mask_positivo & (~mask_negativo)]

colunas_padrao = ['DSC_ESTABELECIMENTO', 'NOM_TITULO_SEGLOGR', 'NOM_SEGLOGR', 'NUM_ENDERECO']

for col in colunas_padrao:
    if col in df_salao.columns:
        if df_salao[col].dtype == 'O' or pd.api.types.is_string_dtype(df_salao[col]):
            df_salao.loc[:, col] = df_salao[col].astype(str).str.strip().str.upper()

df_salao = df_salao.drop_duplicates(subset=[
    'DSC_ESTABELECIMENTO',
    'COD_UNICO_ENDERECO',
    'NOM_TIPO_SEGLOGR',
    'NOM_TITULO_SEGLOGR',
    'NOM_SEGLOGR',
    'NUM_ENDERECO',
    'CEP',
    'LATITUDE',
    'LONGITUDE'
])

colunas_obrigatorias = ['LATITUDE', 'LONGITUDE', 'NOM_SEGLOGR']
df_salao = df_salao.dropna(subset=colunas_obrigatorias)

df_salao['LATITUDE'] = pd.to_numeric(df_salao['LATITUDE'], errors='coerce')
df_salao['LONGITUDE'] = pd.to_numeric(df_salao['LONGITUDE'], errors='coerce')

df_salao = df_salao.dropna(subset=['LATITUDE', 'LONGITUDE'])

# 2. Análise e Extração de Informações

df_salao['NUM_ENDERECO'] = pd.to_numeric(df_salao['NUM_ENDERECO'], errors='coerce')

qtd_por_rua = df_salao['NOM_SEGLOGR'].value_counts()
print("Top 10 ruas com mais salões:")
print(qtd_por_rua.head(10))

print("\nEstatísticas das coordenadas (latitude e longitude):")
print(df_salao[['LATITUDE', 'LONGITUDE']].describe())

print("\nEstatísticas do número do endereço:")
print(df_salao['NUM_ENDERECO'].describe())

top10_ruas = qtd_por_rua.head(10)
plt.figure(figsize=(10,6))
top10_ruas.plot(kind='bar', color='skyblue')
plt.title('Top 10 ruas com mais salões - Gama')
plt.xlabel('Rua')
plt.ylabel('Quantidade de salões')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('top10_ruas_saloes.png')
plt.close()

plt.figure(figsize=(10,5))
df_salao['NUM_ENDERECO'].hist(bins=30, color='coral')
plt.title('Distribuição dos números de endereço')
plt.xlabel('Número do endereço')
plt.ylabel('Frequência')
plt.tight_layout()
plt.savefig('hist_num_endereco.png')
plt.close()

lat_medio = df_salao['LATITUDE'].mean()
lon_medio = df_salao['LONGITUDE'].mean()

mapa = folium.Map(location=[lat_medio, lon_medio], zoom_start=14)

for _, row in df_salao.iterrows():
    folium.Marker(
        location=[row['LATITUDE'], row['LONGITUDE']],
        popup=f"{row['DSC_ESTABELECIMENTO']} - {row['NOM_SEGLOGR']} {row['NUM_ENDERECO']}",
        tooltip=row['DSC_ESTABELECIMENTO']
    ).add_to(mapa)
    
# 3. Apresentação Final    

mapa.save('mapa_saloes_gama.html')
print("\nMapa interativo salvo em 'mapa_saloes_gama.html'.")

print("\nPorcentagem dos salões nas 5 ruas mais comuns:")
top5_ruas = qtd_por_rua.head(5)
porcentagens = (top5_ruas / qtd_por_rua.sum()) * 100
print(porcentagens)

df_salao.to_csv('saloes_filtrados_gama.csv', index=False)
top10_ruas.to_csv('top10_ruas_saloes.csv')
porcentagens.to_csv('porcentagem_top5_ruas.csv')

print("\n✅ Análises finalizadas e arquivos gerados:")
print("- mapa_saloes_gama.html")
print("- saloes_filtrados_gama.csv")
print("- top10_ruas_saloes.png")
print("- hist_num_endereco.png")
print("- top10_ruas_saloes.csv")
print("- porcentagem_top5_ruas.csv")
