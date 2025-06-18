# 📊 Análise de Mercado: Salões de Beleza no Gama (DF)  
**Projeto Prático – Inteligência Artificial com Machine Learning para Negócios**

## 📌 Objetivo

Este projeto visa identificar e analisar a distribuição geográfica dos salões de beleza no bairro **Gama (DF)**, com base nos dados do **Censo do Distrito Federal (2022)**. O foco é fornecer **insights estratégicos** para uma possível **expansão comercial** no setor de beleza.

---

## 🧠 Etapas da Análise

### 1. **Leitura e Limpeza dos Dados**
- Importação da base de dados (`DF.csv`) com registros de atividades comerciais.
- Filtragem da localidade: Gama, Gama Leste e Gama Norte.
- Padronização de colunas (endereços, nomes de estabelecimentos).
- Conversão e validação de coordenadas geográficas.
- Remoção de duplicatas com base em nome, endereço e localização.

### 2. **Filtragem por Tipo de Estabelecimento**
- Seleção de registros com palavras-chave relacionadas a salões de beleza: `SALAO`, `SALÃO`, `BELEZA`.
- Exclusão de registros com palavras irrelevantes como: `IGREJA`, `FESTA`, `DANÇA`, `TESTEMUNHAS`.

### 3. **Análise Descritiva**
- Quantidade de salões por rua.
- Estatísticas dos números de endereço.
- Estatísticas geográficas (latitude e longitude).
- Geração de porcentagens de concentração em ruas mais populares.

### 4. **Visualização Geográfica**
- Geração de um mapa interativo com a localização de todos os salões filtrados.
- Cada marcador contém nome, rua e número do estabelecimento.
- O mapa é salvo como `mapa_saloes_gama.html`.

---

## 📌 Justificativa Analítica

Todas as decisões de filtragem, padronização e exclusão foram guiadas pelos seguintes objetivos:
- Obter uma visão clara, confiável e **sem ruídos** do mercado local.
- Remover registros irrelevantes para o setor de beleza.
- Evitar duplicações que pudessem distorcer a análise de concentração geográfica.
- Preparar uma visualização acessível e prática para consulta de localização.

---

## 🗺️ Resultado da Visualização

📍 O mapa mostra a **distribuição espacial dos salões** na região, facilitando decisões de localização estratégica.

---

## 📂 Arquivos Gerados

- `mapa_saloes_gama.html`: Mapa interativo com os salões geolocalizados.
- `saloes_filtrados_gama.csv`: Base final limpa com os salões analisados.
- `TrabalhoFinal_ProjetoPratico.py`: Script principal do projeto.

---

## 🔧 Tecnologias Utilizadas

- Python
- Pandas
- Folium
- Matplotlib (opcional para gráficos)
- Spyder

---

## 📈 Conclusões

- A maior concentração de salões está em **ruas comerciais centrais** do Gama.
- A limpeza e filtragem eliminaram **estabelecimentos irrelevantes** para o nicho.
- O projeto oferece um **panorama estratégico** para investidores ou gestores que desejam entender o mercado local.

---

## ✍️ Autor

Gustavo Maxwel de Sousa Oliveira  
Curso: Inteligência Artificial com Machine Learning para Negócios  
Data: Junho de 2025
