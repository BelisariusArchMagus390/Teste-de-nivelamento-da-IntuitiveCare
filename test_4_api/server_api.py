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
# get the file path
file_path = Path(__file__).parent
file_path = file_path.joinpath(file_path, "data", "Relatorio_cadop.csv")
# read the csv file
df = pd.read_fwf(file_path, delimiter=";")
# remove the extra black spaces from the column names and for the rest of the rows
df.columns = df.columns.str.strip()
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
# set the route for the research function
@app.get("/search")
# make the research in the dataframe getting the values by a GET
def search_information(input_field: str, column_search: str):
    input_field = input_field.strip().upper() 
    resultado = df[df[column_search].str.replace(r"\s+", " ", regex=True).str.upper().str.contains(input_field, case=False, na=False)]
    return resultado.to_dict(orient="records")