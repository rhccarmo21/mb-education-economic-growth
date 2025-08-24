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

# 📄 Relatórios

## 📋 1. Relatório Executivo (5–6 páginas)

**Público-alvo:** Gestores e formuladores de políticas públicas  
**Objetivo:** Apresentação clara e visual dos principais insights

### 🎯 Estrutura do Conteúdo:
- **📌 Contexto e Justificativa**
  - Importância da relação educação-crescimento econômico
  - Relevância para políticas públicas
- **❓ Perguntas de Pesquisa**
  - Objetivos principais do estudo
  - Questões investigadas
- **📊 Resultados Principais**
  - Gráficos comparativos e visualizações impactantes
  - Principais correlações identificadas
  - Insights por região/grupo de países
- **💡 Implicações para Políticas Públicas**
  - Recomendações estratégicas
  - Diretrizes para investimentos em educação
  - Impacto potencial no crescimento econômico

---

## 🔧 2. Relatório Técnico (10–15 páginas)

**Público-alvo:** Acadêmicos, pesquisadores e avaliadores técnicos  
**Objetivo:** Rigor metodológico e profundidade analítica

### 🎯 Estrutura do Conteúdo:
- **📋 Metodologia Detalhada**
  - Fontes de dados e critérios de seleção
  - Métodos de coleta e tratamento de dados
  - Framework analítico
- **📈 Análises Estatísticas Aprofundadas**
  - Modelos de regressão multivariada
  - Análise de séries temporais
  - Testes de robustez e validação
  - Análise de mediação e moderação
- **⚠️ Discussão de Limitações**
  - Potenciais vieses e limitações metodológicas
  - Considerações sobre causalidade vs. correlação
  - Limitações dos dados disponíveis
- **🔮 Sugestões para Próximos Estudos**
  - Direções futuras de pesquisa
  - Melhorias metodológicas sugeridas
  - Expansões possíveis do estudo

---

## 🛠️ Produção dos Relatórios

### 📝 Sistema de Geração:
- **🔄 Pipeline Integrado LaTeX**
  - Geração automática a partir dos dados processados
  - Templates consistentes para ambos os relatórios
  - Atualização em tempo real com novos resultados

### 🎨 Características Técnicas:
- **✅ Consistência Visual**
  - Design unificado entre documentos
  - Paleta de cores e tipografia padronizadas
  - Layout profissional e acadêmico
- **⚡ Atualização Automática**
  - Vinculação direta com base de dados
  - Geração dinâmica de gráficos e tabelas
  - Atualização de métricas e resultados
- **📊 Integração com Análise**
  - Conexão direta com notebooks Jupyter
  - Exportação automática de visualizações
  - Inclusão de código estatístico quando relevante

### 📦 Entregáveis:
- **📄 Versão PDF** - Formatada profissionalmente
- **📝 Código Fonte LaTeX** - Para modificações futuras
- **📊 Dados Suplementares** - Conjuntos de dados processados
- **🖼️ Visualizações Separadas** - Gráficos em alta resolução
