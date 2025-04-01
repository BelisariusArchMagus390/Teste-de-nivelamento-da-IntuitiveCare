from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from pathlib import Path
import csv

def search_information(input_field: str = Query(...), column_search: str = Query(...)):
    input_field = input_field.strip().upper() 
    resultado = df[df[column_search].str.replace(r"\s+", " ", regex=True).str.upper().str.contains(input_field, case=False, na=False)]
    return resultado.to_dict(orient="records")

# Caminho do arquivo CSV
file_path = Path(__file__).parent
file_path = file_path.joinpath(file_path, "data", "Relatorio_cadop.csv")
# print(file_path)

# df = pd.read_csv(file_path_csv, na_values="None")
df = pd.read_fwf(file_path, delimiter=";")

df.columns = df.columns.str.strip()
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

lol = search_information("19541931000125", "CNPJ")

print(lol)
#print(lol)

#for i in df.columns.to_list():
#    print(i)