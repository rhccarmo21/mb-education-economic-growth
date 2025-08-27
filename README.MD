# 📊 Educação e Crescimento Econômico

## 🌍 Contexto
Este estudo investiga a relação entre **desenvolvimento econômico** e **investimentos/níveis de escolaridade**, utilizando dados oficiais do **Banco Mundial**.  
A motivação é compreender em que medida a **educação** pode ser considerada motor do crescimento de longo prazo, especialmente em países em desenvolvimento.

O trabalho faz parte de um portfólio de projetos em **Ciência de Dados aplicada a Políticas Públicas**, buscando traduzir evidências em insights úteis para gestores, pesquisadores e cidadãos.

---

## 📋 Visão Geral
- **Fonte de dados**: Banco Mundial (World Development Indicators).  
- **Período analisado**: 2000–2023.  
- **Países incluídos**: 200+ nações com dados disponíveis.  
- **Indicadores principais**:
  - PIB per capita (crescimento econômico).  
  - Despesa pública em educação (% do PIB).  
  - Taxa líquida de matrícula no ensino primário e secundário.  

---

## 🛠️ Metodologia
1. **Coleta de dados** via API do Banco Mundial.  
2. **Limpeza e padronização** dos indicadores para garantir comparabilidade entre países.  
3. **Análises estatísticas**:
   - Correlação entre variáveis.  
   - Visualizações comparativas por região e nível de renda.  
   - Tendências temporais.  
4. **Geração de gráficos** para apoiar a interpretação dos resultados.

---

## 📈 Resultados Principais
A seguir, alguns dos gráficos produzidos no estudo.  

### 1. Relação entre gasto em educação e crescimento econômico
📌 *Comentário*: Observa-se uma **correlação positiva**: países que investem percentualmente mais em educação tendem a apresentar maiores taxas de crescimento de longo prazo, embora haja dispersão relevante.

---

### 2. Escolaridade e renda per capita
📌 *Comentário*: Aumentos na taxa de matrícula, sobretudo no ensino secundário, estão associados a **PIB per capita mais elevado**. Regiões como a Ásia Oriental apresentam ganhos mais consistentes nesse aspecto.

---

### 3. Diferenças regionais
📌 *Comentário*: A relação educação ↔ crescimento não é homogênea. Países da África Subsaariana mostram **alto esforço relativo em educação**, mas com retornos econômicos ainda limitados, indicando a presença de outros gargalos estruturais.

---

## 🔎 Conclusão
O estudo reforça a visão de que **educação é condição necessária, mas não suficiente, para o crescimento econômico sustentável**.  
- Em economias emergentes, o investimento em educação precisa ser acompanhado de reformas institucionais e de mercado para gerar impacto duradouro.  
- Já em países desenvolvidos, a escolaridade elevada consolida ganhos de produtividade e inovação.  

📌 **Implicação para políticas públicas**: expandir o acesso e melhorar a qualidade educacional são estratégias fundamentais, mas precisam ser integradas a políticas econômicas mais amplas.

---

## ⚙️ Como Reproduzir
Clone este repositório e rode o notebook principal:

```bash
git clone https://github.com/rhccarmo21/mb-education-economic-growth.git
cd mb-education-economic-growth
jupyter notebook
