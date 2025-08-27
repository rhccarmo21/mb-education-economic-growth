# consolidate_datasets.py
import pandas as pd
import os

# Diretório dos dados
data_dir = "./data"
output_dir = "./output"
os.makedirs(output_dir, exist_ok=True)

# Arquivos CSV que queremos usar (ignorando metadados)
csv_files = [
    "API_GB.XPD.RSDV.GD.ZS_DS2_en_csv_v2_408555.csv",   # Gastos com educação (% do PIB)
    "API_SE.XPD.TOTL.GD.ZS_DS2_en_csv_v2_408324.csv",   # Gasto total em educação (% do PIB)
    "API_NY.GDP.PCAP.PP.CD_DS2_en_csv_v2_409116.csv",   # PIB per capita (PPC)
    "API_SE.SEC.CUAT.UP.ZS_DS2_en_csv_v2_23900.csv",    # Taxa de matrícula secundária
    "API_SE.SEC.ENRR_DS2_en_csv_v2_394206.csv",         # Taxa de matrícula total
    "API_SI.POV.GINI_DS2_en_csv_v2_408161.csv"          # Coeficiente de Gini
]

# Função para ler e tratar CSV do Banco Mundial
def load_wb_csv(file_path):
    try:
        # Pula as primeiras 4 linhas de metadados
        df = pd.read_csv(file_path, skiprows=4)
        # Mantém apenas colunas numéricas + identificação do país
        years = [col for col in df.columns if col.isdigit()]
        df_long = df.melt(
            id_vars=["Country Name", "Country Code"],
            value_vars=years,
            var_name="Year",
            value_name="Value"
        )
        df_long["Year"] = df_long["Year"].astype(int)
        df_long["Value"] = pd.to_numeric(df_long["Value"], errors="coerce")
        return df_long
    except Exception as e:
        print(f"Erro ao processar {file_path}: {e}")
        return None

# Dicionário para armazenar DataFrames
dfs = {}

# Carrega cada CSV
for file in csv_files:
    path = os.path.join(data_dir, file)
    print(f"Carregando {file} ...")
    df = load_wb_csv(path)
    if df is not None:
        key = file.split("_")[1]  # usa o código do indicador como chave
        dfs[key] = df
        print(f"✅ {file} carregado: {df.shape[0]} linhas")

# Agora vamos consolidar os dados pelo país e ano
# Iniciamos com PIB per capita como referência
df_master = dfs["NY.GDP.PCAP.PP.CD"]

for key, df in dfs.items():
    if key == "NY.GDP.PCAP.PP.CD":
        continue
    # Merge pelo país e ano
    df_master = df_master.merge(
        df,
        on=["Country Name", "Country Code", "Year"],
        how="left",
        suffixes=("", f"_{key}")
    )

# Salva CSV consolidado para análise
consolidated_path = os.path.join(output_dir, "consolidated_wb_data.csv")
df_master.to_csv(consolidated_path, index=False)
print(f"\n📊 Dados consolidados salvos em: {consolidated_path}")
print("🎯 Agora você tem um DataFrame pronto para análise de correlação entre educação e PIB per capita!")
