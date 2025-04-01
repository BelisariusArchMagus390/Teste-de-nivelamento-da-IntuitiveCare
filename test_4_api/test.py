from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from pathlib import Path
import csv

def buscar_operadora(registro_ans: str = Query(..., min_length=1)):
    registro_ans = registro_ans.strip().upper()  # Remove espaços extras e converte para uppercase
    resultado = df[df["Registro_ANS"].str.replace(r"\s+", " ", regex=True).str.upper().str.contains(registro_ans, case=False, na=False)]
    return resultado.to_dict(orient="records")

# Caminho do arquivo CSV
file_path = Path(__file__).parent
file_path = file_path.joinpath(file_path, "data", "Relatorio_cadop.csv")
# print(file_path)

# df = pd.read_csv(file_path_csv, na_values="None")
df = pd.read_fwf(file_path, delimiter=";")

df.columns = df.columns.str.strip()
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

lol = buscar_operadora("419761")

print(lol)