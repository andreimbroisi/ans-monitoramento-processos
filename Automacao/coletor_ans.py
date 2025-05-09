# Feito por André Imbroisi Martins Borba
import pandas as pd
import json
from pathlib import Path

# Arquivo Excel
arquivo = Path("Automacao/exemplos_dados/ans_2024.xlsx")

# Carregando a planilha
df = pd.read_excel(arquivo)

# Convertendo datas do tipo Timestamp para string
for coluna in df.select_dtypes(include=["datetime64[ns]"]).columns:
    df[coluna] = df[coluna].astype(str)

# Tratando valores nulos com boas práticas
for coluna in df.columns:
    if df[coluna].dtype in ["float64", "int64"]:
        df[coluna] = df[coluna].fillna(0)  # Preenche números com 0
    else:
        df[coluna] = df[coluna].fillna("N/A")  # Preenche texto com "N/A"

# Convertendo DataFrame em lista de dicionários
dados_dict = df.to_dict(orient="records")

# Caminho para o JSON
output_path = Path("Automacao/relatorio_ans.json")
output_path.parent.mkdir(parents=True, exist_ok=True)

# Salvando os dados no formato JSON
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(dados_dict, f, indent=4, ensure_ascii=False)

print("Exportado com sucesso para:", output_path.resolve())
