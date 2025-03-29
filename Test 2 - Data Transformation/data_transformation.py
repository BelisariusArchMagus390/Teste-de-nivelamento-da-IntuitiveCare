from pathlib import Path
import tabula
import pandas as pd
from IPython.display import display

name_file_pdf = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
name_file_csv = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.csv"

# path of the pdf file
file_path_pdf = file_path.joinpath(file_path, directory_path, name_file_pdf);


# path of the csv file
file_path_csv = file_path.joinpath(file_path, directory_path, name_file_csv);


file_path_csv = file_path.joinpath(file_path, directory_path, name_file_csv);

dataframe_tables = pd.read_csv(file_path_csv)

# replace the values "OD" and "AMB" for "Seg. Odontológica" and "Seg. Ambulatorial" in your respective columns
dataframe_tables[["OD","AMB"]] = dataframe_tables[["OD","AMB"]].replace(["OD", "AMB"], ["Seg. Odontológica", "Seg. Ambulatorial"])

file_path_excel = file_path.joinpath(file_path, directory_path, "teste.xlsx");
dataframe_tables.to_excel(file_path_excel)
print("Nice")

class DataTransformationPDFtoCSV:
    def __init__(self):
        self.file_path_pdf = None
        self.file_path_csv = None
        self.tables_dataframe = None
    
    def get_path(self, name_file):
        # path of the file data_transformation.py
        file_path = Path(__file__).parent
        directory_path = Path("data")
        # return the path of the file
        file_path_pdf = file_path.joinpath(file_path, directory_path, name_file)
        return file_path_pdf

    def get_table(self, name_file_pdf):
        self.file_path_pdf = self.get_path(name_file_pdf)
        # reading pdf file
        self.tables_dataframe = tabula.read_pdf(self.file_path_pdf, pages="3-181", lattice=True, multiple_tables=True)
        # concat the tables of all pages and reset the index of dataframe
        self.tables_dataframe = pd.concat(self.tables_dataframe).reset_index(drop=True)

    def dataframe_to_csv(self, name_file_csv):
        self.file_path_csv = self.get_path(name_file_csv)
        # create the csv file
        self.tables_dataframe.to_csv(self.file_path_csv)

    def rename_column(self, old_collumn_name, new_collumn_name):
        # rename the columns
        dataframe_tables = dataframe_tables.rename(columns={old_collumn_names[0]: new_collumn_names[0], old_collumn_names[1]: new_collumn_names[1]})