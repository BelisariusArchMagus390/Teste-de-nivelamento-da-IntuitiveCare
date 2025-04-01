from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from pathlib import Path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

file_path = Path(__file__).parent
file_path = file_path.joinpath(file_path, "data", "Relatorio_cadop.csv")

df = pd.read_fwf(file_path, delimiter=";")

df.columns = df.columns.str.strip()
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

@app.get("/buscar")
def buscar_operadora(registro_ans: str = Query(..., min_length=1)):
    registro_ans = registro_ans.strip().upper()  # Remove espaços extras e converte para uppercase
    resultado = df[df["Registro_ANS"].str.replace(r"\s+", " ", regex=True).str.upper().str.contains(registro_ans, case=False, na=False)]
    return resultado.to_dict(orient="records")

#@app.get("/buscar")
#def buscar_operadora(razao_social: str = Query(..., min_length=1)):
#    resultado = df[df["Razao_Social"].str.contains(razao_social, case=False, na=False)]
#    return resultado.to_dict(orient="records")