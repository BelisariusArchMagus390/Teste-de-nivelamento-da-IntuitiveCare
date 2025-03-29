from data_transformation import DataTransformationPDFtoCSV

original_name_file = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
name_file_csv = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.csv"

dt_transform = DataTransformationPDFtoCSV()

dt_transform.get_table(original_name_file)

dt_transform.rename_column("OD", "Seg. Odontológica")