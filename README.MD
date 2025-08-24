# 📊 Projeto: Educação e Crescimento Econômico

## 🌍 Visão Geral
Este projeto investiga a relação entre **educação** e **crescimento econômico**, explorando dados de múltiplas fontes globais para compreender como indicadores educacionais influenciam o desenvolvimento econômico de países e regiões.

O objetivo é identificar **correlações, padrões e possíveis implicações de políticas públicas** que possam reforçar a importância do investimento em educação para o crescimento sustentável.

---

## ❓ Perguntas de Pesquisa
O projeto busca responder a questões centrais como:

1.  Existe uma relação estatisticamente significativa entre indicadores educacionais (taxa de matrícula, anos médios de escolaridade, gasto público em educação) e crescimento econômico (PIB per capita, crescimento anual do PIB)?
2.  Quais regiões ou grupos de países apresentam maior eficiência na transformação de investimentos em educação em crescimento econômico?
3.  O efeito da educação no crescimento é linear, ou existem pontos de saturação (diminuição dos retornos marginais)?
4.  Quais variáveis socioeconômicas intermediárias (desigualdade, mercado de trabalho, inovação tecnológica) mediam essa relação?
5.  Há indícios de causalidade (educação → crescimento) ou apenas correlação?

---

## 🔗 Fontes de Dados / APIs
Este projeto se apoia em bases de dados internacionais, acessadas preferencialmente via APIs:

-   **UNESCO Institute for Statistics (UIS API)** → Indicadores educacionais globais.
-   **Banco Mundial (World Bank API / World Development Indicators)** → PIB, crescimento econômico, indicadores sociais.
-   **OECD API** → Indicadores comparativos de educação e produtividade.
-   **UNDP (Human Development Reports API)** → Índice de Desenvolvimento Humano e variáveis socioeconômicas.
-   **ILO (International Labour Organization API)** → Mercado de trabalho e empregabilidade.

---

## ⚙️ Requisitos (`requirements.txt`)
As principais bibliotecas utilizadas serão:

```txt
pandas
numpy
matplotlib
seaborn
scikit-learn
statsmodels
jupyter
requests
sqlalchemy
plotly
latex
pylatex

📂 Estrutura do Projeto
mb-education-economic-growth/
│
├── data/                    # Dados brutos e processados
│   ├── raw/                 # Dados originais das APIs
│   ├── processed/           # Dados tratados para análise
│
├── notebooks/               # Jupyter Notebooks com análises exploratórias
│   ├── 01_exploracao.ipynb
│   ├── 02_modelagem.ipynb
│
├── reports/                 # Relatórios em LaTeX
│   ├── executive/           # Relatório executivo (5–6 páginas)
│   ├── technical/           # Relatório técnico (10–15 páginas)
│
├── src/                     # Código-fonte do projeto
│   ├── data/                # Scripts de coleta e tratamento de dados
│   ├── analysis/            # Scripts de análise estatística
│   ├── visualization/       # Funções de visualização
│
├── requirements.txt         # Dependências do projeto
├── README.md                # Documento atual

📄 Relatórios
1. Relatório Executivo (5–6 páginas)
Público-alvo: Gestores e policy makers
Foco: Clareza e impacto visual

Conteúdo Principal:

Contexto e justificativa

Perguntas de pesquisa

Resultados principais com gráficos comparativos

Implicações para políticas públicas

2. Relatório Técnico (10–15 páginas)
Público-alvo: Avaliadores técnicos e acadêmicos
Foco: Rigor metodológico e profundidade analítica

Conteúdo Principal:

Metodologia detalhada

Análises estatísticas aprofundadas (regressões, séries temporais, robustez)

Discussão de limitações e potenciais vieses

Sugestões de próximos estudos

🎯 Produção dos Relatórios
Ambos os relatórios serão:

Gerados em LaTeX a partir do mesmo pipeline

Garantem consistência visual entre documentos

Permitem atualização automática dos dados e resultados

Produzidos de forma integrada com a análise de dados
