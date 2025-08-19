import pandas as pd
import glob
import os

def run_etl():
    # Caminho da pasta onde estão os arquivos de entrada
    raw_path = r"C:\Users\55349\Downloads\Teste de BI - Pleno_1408\data\raw"
    refined_path = r"C:\Users\55349\Downloads\Teste de BI - Pleno_1408\data\refined"
    os.makedirs(refined_path, exist_ok=True)

    # Busca todos os arquivos no formato financial_data_*.csv
    files = glob.glob(os.path.join(raw_path, "financial_data_*.csv"))
    print("Arquivos encontrados:", files)

    dataframes = []

    for file in files:
        # Extrai o ano do nome do arquivo (ex: financial_data_2023.csv → 2023)
        source_date = os.path.basename(file).split("_")[-1].replace(".csv", "")

        # Lê o CSV
        df = pd.read_csv(file)

        # Adiciona a coluna SourceDate
        df["SourceDate"] = int(source_date)

        dataframes.append(df)

    # Empilha todos em um único DataFrame
    final_df = pd.concat(dataframes, ignore_index=True)

    # Ajusta os tipos de dados
    final_df["TransactionID"] = final_df["TransactionID"].astype("string")
    final_df["CustomerID"] = final_df["CustomerID"].astype("string")
    final_df["Date"] = pd.to_datetime(final_df["Date"], format="%Y-%m-%d")
    final_df["TransactionType"] = final_df["TransactionType"].astype("category")
    final_df["PaymentMethod"] = final_df["PaymentMethod"].astype("category")
    final_df["Status"] = final_df["Status"].astype("category")
    final_df["Region"] = final_df["Region"].astype("category")
    final_df["SourceDate"] = final_df["SourceDate"].astype("int")

    # Colunas numéricas
    numeric_cols = ["Amount", "Discount", "Tax", "ShippingCost", "Total"]
    final_df[numeric_cols] = final_df[numeric_cols].apply(pd.to_numeric, errors="coerce")

    # Salva em CSV consolidado
    output_file = os.path.join(refined_path, "fato_financial_data.csv")
    final_df.to_csv(output_file, index=False)

    print(f"Arquivo consolidado gerado em: {output_file}")
    print(f"Total de registros consolidados: {len(final_df)}")

if __name__ == "__main__":
    run_etl()
