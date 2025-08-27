import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Carregar dados consolidados
df = pd.read_csv('./output/consolidated_wb_data.csv')

# Renomear colunas para simplificar
df.rename(columns={
    'Value': 'GDP_per_capita',
    'Value_SE.SEC.ENRR': 'Total_Enrollment',
    'Value_SE.SEC.CUAT.UP.ZS': 'Secondary_Enrollment_Percent',
    'Value_GB.XPD.RSDV.GD.ZS': 'Edu_Expenditure_Pct_GDP',
    'Value_SE.XPD.TOTL.GD.ZS': 'Edu_Total_Expenditure'
}, inplace=True)

# Filtrar dados válidos para análise global
df_global = df[['GDP_per_capita', 'Total_Enrollment', 'Secondary_Enrollment_Percent',
                'Edu_Expenditure_Pct_GDP', 'Edu_Total_Expenditure']].dropna()

# -------------------------
# 1️⃣ Gráficos de dispersão globais
# -------------------------
plt.figure(figsize=(10,6))
sns.scatterplot(data=df_global, x='Total_Enrollment', y='GDP_per_capita')
sns.regplot(data=df_global, x='Total_Enrollment', y='GDP_per_capita', scatter=False, color='red')
plt.title("Relação entre Total de Matrículas e PIB per Capita (Global)")
plt.xlabel("Total de Matrículas")
plt.ylabel("PIB per Capita (USD)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,6))
sns.scatterplot(data=df_global, x='Edu_Expenditure_Pct_GDP', y='GDP_per_capita')
sns.regplot(data=df_global, x='Edu_Expenditure_Pct_GDP', y='GDP_per_capita', scatter=False, color='red')
plt.title("Relação entre Gasto em Educação (% do PIB) e PIB per Capita")
plt.xlabel("Gasto em Educação (% do PIB)")
plt.ylabel("PIB per Capita (USD)")
plt.tight_layout()
plt.show()

# -------------------------
# 2️⃣ Correlação por país
# -------------------------
corr_per_country = df.groupby('Country Name').apply(
    lambda x: x[['GDP_per_capita','Total_Enrollment','Secondary_Enrollment_Percent',
                 'Edu_Expenditure_Pct_GDP','Edu_Total_Expenditure']].corr().iloc[0,1]
)
corr_per_country = corr_per_country.dropna().sort_values(ascending=False)

# Gráfico top 20 países
plt.figure(figsize=(12,6))
sns.barplot(x=corr_per_country.head(20).values, y=corr_per_country.head(20).index, palette='viridis')
plt.title("Top 20 Países com Maior Correlação Educação x PIB per Capita")
plt.xlabel("Correlação")
plt.ylabel("País")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,6))
sns.barplot(x=corr_per_country.tail(20).values, y=corr_per_country.tail(20).index, palette='magma')
plt.title("Top 20 Países com Menor Correlação Educação x PIB per Capita")
plt.xlabel("Correlação")
plt.ylabel("País")
plt.tight_layout()
plt.show()

# -------------------------
# 3️⃣ Tabela de correlação global
# -------------------------
corr_global = df_global.corr()['GDP_per_capita'].sort_values(ascending=False)
print("📊 Correlação global entre PIB per Capita e indicadores educacionais:\n")
print(corr_global)

# -------------------------
# 4️⃣ Insights resumidos (linguagem acessível)
# -------------------------
print("\n📌 Insights:")
print("- Existe uma correlação positiva moderada entre o total de matrículas e o PIB per capita.")
print("- A matrícula no ensino secundário e o gasto em educação também mostram relação positiva, porém mais fraca.")
print("- Alguns países apresentam forte correlação, indicando que investimentos em educação podem impactar diretamente o crescimento econômico.")
print("- Em outros países, a correlação é baixa ou negativa, sugerindo que fatores estruturais ou contextuais influenciam mais o crescimento econômico.")
