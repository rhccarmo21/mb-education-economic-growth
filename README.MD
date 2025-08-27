# 📊 Educação e Crescimento Econômico: Evidências de 200+ Países

Este estudo integra **Ciência de Dados** e **Políticas Públicas** para investigar a relação entre **investimentos educacionais** e **crescimento econômico**. Utilizamos dados do **Banco Mundial** cobrindo mais de **200 países** ao longo de vários anos, com foco em como matrículas, gastos em educação e participação no PIB se correlacionam com o **PIB per capita**.

---

## 🔍 Metodologia

- **Fonte de dados:** Banco Mundial (indicadores de educação e economia).
- **Variáveis principais analisadas:**
  - PIB per capita (GDP per capita)
  - Matrículas totais em todos os níveis (Total Enrollment)
  - Matrículas no ensino secundário (% da população em idade escolar)
  - Gastos em educação (% do PIB)
  - Gastos totais em educação (valores absolutos)
- **Técnica utilizada:** análise de correlação de Pearson entre indicadores de educação e PIB per capita, tanto em nível global quanto por país.

---

## 📊 Resultados

### 1. Correlação global entre educação e PIB per capita

| Indicador de Educação | Correlação com PIB per capita |
|------------------------|-------------------------------|
| Total Enrollment       | **0.476** |
| Secondary Enrollment % | **0.288** |
| Education Expenditure % GDP | **0.272** |
| Total Expenditure (absolute) | **0.094** |

➡️ **Interpretação:**  
De forma geral, países com **maior taxa de matrículas** e **maior percentual de gastos em educação** apresentam níveis mais altos de PIB per capita. No entanto, a força dessas correlações é **moderada**, sugerindo que a educação é importante, mas não o único fator determinante do desenvolvimento econômico.

---

### 2. Correlação por país (indicadores educacionais x PIB per capita)

A análise país a país revela grande variação:

- **Correlação positiva moderada** em países como **Albânia (0.115)** e **Argélia (0.129)**, indicando que aumentos em matrículas e investimentos em educação tendem a acompanhar o crescimento econômico.
- **Correlação negativa** em países como **Zâmbia (-0.391)** e **West Bank and Gaza (-0.350)**, sugerindo que maiores gastos não necessariamente se traduzem em crescimento, possivelmente devido a fatores estruturais, instabilidade política ou ineficiências no sistema educacional.
- **Muitos países apresentam correlação fraca ou próxima de zero**, revelando que o impacto da educação sobre o crescimento econômico é fortemente mediado por outros fatores locais (governança, desigualdade, setor produtivo, etc.).

---

## 🧩 Conclusões

- **Educação importa:** Existe uma correlação clara entre melhores indicadores educacionais e níveis mais altos de renda per capita.
- **Mas não basta investir:** O simples aumento nos gastos não garante crescimento. É necessário que o investimento seja **efetivo**, bem distribuído e acompanhado de políticas de desenvolvimento econômico.
- **O contexto importa:** Em países com fragilidade institucional ou desigualdades profundas, os ganhos econômicos da educação podem ser limitados.
- **Próximos passos:** Pesquisas futuras podem combinar análise de causalidade e modelos explicativos para compreender melhor **como** e **quando** a educação se transforma em crescimento econômico.

---

## 📂 Estrutura do Repositório

- `data/` → bases utilizadas (Banco Mundial)  
- `notebooks/` → análises exploratórias e correlações  
- `figures/` → gráficos e visualizações  
- `results/` → tabelas de saída e indicadores finais  

---

✍️ **Autor:** Roberto C.  
🔗 [Perfil GitHub](https://github.com/rhccarmo21) | [LinkedIn](#)  

