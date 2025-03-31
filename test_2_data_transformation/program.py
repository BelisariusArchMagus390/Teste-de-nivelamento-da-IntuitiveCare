from data_transformation import DataTransformationPDFtoCSV

original_file_name = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
csv_file_name = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.csv"
excel_file_name = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.xlsx"
zip_file_name = "Teste_Gustavo.zip"

dt_transform = DataTransformationPDFtoCSV()
# read the pdf  and create a dataframe
dt_transform.get_table(original_file_name)

# replacing values
dt_transform.replace_values("OD", "OD", "Seg. Odontológica")
dt_transform.replace_values("AMB", "AMB", "Seg. Ambulatorial")

# rename columns
dt_transform.rename_column("OD", "Seg. Odontológica")
dt_transform.rename_column("AMB", "Seg. Ambulatorial")

# transforn in others file formats
dt_transform.dataframe_to_csv(csv_file_name)
dt_transform.dataframe_to_excel(excel_file_name)

# compact the csv file
dt_transform.compact_file(csv_file_name, zip_file_name)