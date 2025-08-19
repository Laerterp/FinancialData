import sqlite3
import pandas as pd
import os

def main():
    # Caminho do banco SQLite
    db_path = os.path.join(os.path.dirname(__file__), "..", "..", "financial_dw.db")

    # Conexão com o banco
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        # Caminho do arquivo SQL (mesma pasta do script)
        sql_file = os.path.join(os.path.dirname(__file__), "create_view_vw_financial.sql")
        
        # Executa o script SQL para criar ou atualizar a view
        with open(sql_file, "r", encoding="utf-8") as f:
            cursor.executescript(f.read())
        print("View vw_financial criada/atualizada com sucesso.")

        # Consulta para validar os dados da view
        df = pd.read_sql_query("SELECT * FROM vw_financial LIMIT 10;", conn)
        print("\n Primeiros 10 registros da view vw_financial:")
        print(df)

    except Exception as e:
        print("Erro ao criar ou consultar a view:", e)

    finally:
        conn.close()

if __name__ == "__main__":
    main()
