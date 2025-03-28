from pathlib import Path
import tabula
import pandas as pd
from IPython.display import display

name_file_pdf = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
name_file_csv = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.csv"

file_path = Path(__file__).parent
directory_path = Path("data")

# path of the pdf file
file_path_pdf = file_path.joinpath(file_path, directory_path, name_file_pdf);
# reading pdf file
# tables = tabula.read_pdf(file_path_pdf, pages="3-181", lattice=True, multiple_tables=True)
# concat the tables of all pages and reset the index of dataframe
# dataframe_tables = pd.concat(tables).reset_index(drop=True)

# path of the csv file
# file_path_csv = file_path.joinpath(file_path, directory_path, name_file_csv);
# create the csv file
# dataframe_tables.to_csv(file_path_csv)

file_path_csv = file_path.joinpath(file_path, directory_path, name_file_csv);

dataframe_tables = pd.read_csv(file_path_csv)
#dataframe_tables = dataframe_tables.replace(["OD", "Seg. Odontológica"], ["AMB", "Seg. Ambulatorial"])

# replace the values "OD" and "AMB" for "Seg. Odontológica" and "Seg. Ambulatorial" in your respective columns
dataframe_tables[["OD","AMB"]] = dataframe_tables[["OD","AMB"]].replace(["OD", "AMB"], ["Seg. Odontológica", "Seg. Ambulatorial"])
# rename the columns "OD" and "AMB" for "Seg. Odontológica" and "Seg. Ambulatorial"
dataframe_tables = dataframe_tables.rename(columns={"OD": "Seg. Odontológica","AMB": "Seg. Ambulatorial"})

file_path_excel = file_path.joinpath(file_path, directory_path, "teste.xlsx");
dataframe_tables.to_excel(file_path_excel)
print("Nice")

# class DataTransformationPDFtoCSV():