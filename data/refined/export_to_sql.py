import pandas as pd
from sqlalchemy import create_engine
import os
import datetime

def export_to_sql():
    log_file = "export_log.txt"
    try:
        # Caminhos dos arquivos CSV
        fato_file = "data/refined/fato_financial_data.csv"
        dim_file = "data/dim_raw/dim_customer_data.csv"

        # Conexão com o banco SQLite (arquivo será criado no diretório atual)
        engine = create_engine("sqlite:///financial_dw.db")

        # Carrega os dados
        df_fato = pd.read_csv(fato_file)
        df_dim = pd.read_csv(dim_file)

        # Exporta os dados para o SQLite
        df_fato.to_sql("fato_financial_data", engine, if_exists="replace", index=False)
        df_dim.to_sql("dim_customer_data", engine, if_exists="replace", index=False)

        # Log de sucesso
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.datetime.now()}] Exportação concluída com sucesso.\n")
        print("Exportação concluída com sucesso.")

    except Exception as e:
        # Log de falha
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.datetime.now()}] Erro na exportação: {str(e)}\n")
        print("Erro na exportação:", e)

if __name__ == "__main__":
    export_to_sql()
