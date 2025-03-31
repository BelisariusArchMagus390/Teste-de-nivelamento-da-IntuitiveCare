from pathlib import Path
import tabula
import pandas as pd
import zipfile
# from IPython.display import display
class DataTransformationPDFtoCSV:
    def __init__(self):
        self.tables_dataframe = None
    
    def get_path(self, name_file):
        # path of the file data_transformation.py
        file_path = Path(__file__).parent
        directory_path = Path("data")
        # return the path of the file
        file_path_pdf = file_path.joinpath(file_path, directory_path, name_file)
        return file_path_pdf

    def get_table(self, name_file_pdf):
        file_path_pdf = self.get_path(name_file_pdf)
        # reading pdf file
        self.tables_dataframe = tabula.read_pdf(file_path_pdf, pages="3-181", lattice=True, multiple_tables=True, encoding='latin1')
        # concat the tables of all pages and reset the index of dataframe
        self.tables_dataframe = pd.concat(self.tables_dataframe).reset_index(drop=True)

        print("Table created")

    def dataframe_to_csv(self, name_file_csv):
        file_path_csv = self.get_path(name_file_csv)
        # create the csv file
        self.tables_dataframe.to_csv(file_path_csv)

        print(f"CSV file {name_file_csv} created")

    def dataframe_to_excel(self, name_file_excel):
        file_path_excel = self.get_path(name_file_excel)
        # create the csv file
        self.tables_dataframe.to_excel(file_path_excel)

        print(f"Excel file {name_file_excel} created")

    def rename_column(self, collumn_name, new_collumn_name):
        # rename the columns
        self.tables_dataframe = self.tables_dataframe.rename(columns={collumn_name: new_collumn_name})

        print(f"Column {collumn_name} renamed to {new_collumn_name}")

    def replace_values(self, column_name, value, new_value):
        # replace the old values for the new ones
        # self.tables_dataframe[["OD","AMB"]] = self.tables_dataframe[["OD","AMB"]].replace(["OD", "AMB"], ["Seg. Odontológica", "Seg. Ambulatorial"])
        self.tables_dataframe[column_name] = self.tables_dataframe[column_name].replace(value, new_value)

        print(f"Value {value} replace to {new_value} in the column {column_name}")

    def compact_file(self, csv_file_name, zip_file_name):
        zip_file_name_path = self.get_path(zip_file_name)
        file_path_csv = self.get_path(csv_file_name)
		# create the zip file
        with zipfile.ZipFile(zip_file_name_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(file_path_csv, file_path_csv.name)

        print(f"All the files have compacted in the file {zip_file_name}.")